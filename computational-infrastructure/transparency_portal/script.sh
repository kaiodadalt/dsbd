#!/bin/bash

if [ $# -lt 4 ]; then
    echo "Erro: São necessários quatro parâmetros: dia inicial, dia final, mês e ano."
    exit 1
fi

# Variáveis que indicam os dias do mês da busca
inicioPeriodo=$1
fimPeriodo=$2

#Variáveis indicando o mês e o ano que irá buscar
mes=$3
ano=$4

if [ $inicioPeriodo -lt 1 -o $inicioPeriodo -gt 31 ]; then
    echo "Erro: O dia inicial deve ser um número entre 1 e 31."
    exit 1
fi

if [ $fimPeriodo -lt 1 -o $fimPeriodo -gt 31 ]; then
    echo "Erro: O dia final deve ser um número entre 1 e 31."
    exit 1
fi

if [ $mes -lt 1 -o $mes -gt 12 ]; then
    echo "Erro: O mês deve ser um número entre 1 e 12."
    exit 1
fi

if [ $ano -lt 2013 -o $ano -gt 2024 ]; then
    echo "Erro: O ano deve ser um número entre 2013 e 2024."
    exit 1
fi

# Este exemplo baixa os dados dos cinco primeiros dias de um determinado mês e ano 
# que são passados como parâmetros para o script
# Um exemple de execução do script é: ./baixaDadosTransp.sh 05 2015

#set -x
#  Indicando qual o endereço do site - Link Novo
siteDownload="https://dadosabertos-download.cgu.gov.br/PortalDaTransparencia/saida/despesas"

# Diretórios que serão utilizados para baixar os dados e processá-los
dataDir="./dados"
tmpDir="./tmp"

# cria diretório
mkdir $dataDir
mkdir $tmpDir

# formata os parâmetros
inicioPeriodo=$(printf "%02d" $1)
fimPeriodo=$(printf "%02d" $2)
mes=$(printf "%02d" $3)

primeiroArquivo=1

# Executa o for para cada dia (inicio e fim) do período
for dia in $(seq -f "%02g" $inicioPeriodo $fimPeriodo); do
  zipFile=$ano$mes$dia'_Despesas.zip'

  # O comando wget vai baixar o arquivo zip com os dados do site 
  echo -n "Baixando arquivo $zipFile ..."
  wget $siteDownload/$zipFile 2> /dev/null
  echo OK

  # Aqui os dados são descompactados no diretório temporário
  echo -n "Descompactando arquivo $zipFile ..."
  unzip -o $zipFile '*_Despesas_Empenho.csv' '*_Despesas_Pagamento.csv' -d $tmpDir 
  echo OK

  # Remove a primeira linha dos arquivos descompactados, caso não seja a primeira iteração do for
  if [ $primeiroArquivo != 1 ]; then
    echo -n "Removendo primeira linha dos arquivos descompactados ..."
    tail -n +2 "${tmpDir}/${ano}${mes}${dia}_Despesas_Empenho.csv" > "file.tmp" && mv "file.tmp" "${tmpDir}/${ano}${mes}${dia}_Despesas_Empenho.csv"
    tail -n +2 "${tmpDir}/${ano}${mes}${dia}_Despesas_Pagamento.csv" > "file.tmp" && mv "file.tmp" "${tmpDir}/${ano}${mes}${dia}_Despesas_Pagamento.csv" 
    echo OK
  fi

  primeiroArquivo=0

  # Arquivo zip é removido
  echo -n "Removendo arquivo $zipFile ..."
  rm -f $zipFile
  echo OK
done

# Dados são copiados do diretório temporário para o diretório dados
cat $tmpDir/*_Despesas_Empenho.csv > "$dataDir/${ano}${mes}${inicioPeriodo}-${fimPeriodo}_Despesas_Empenho.csv"
cat $tmpDir/*_Despesas_Pagamento.csv > "$dataDir/${ano}${mes}${inicioPeriodo}-${fimPeriodo}_Despesas_Pagamento.csv"

# Diretório temporário é apagado
rm -rf $tmpDir
