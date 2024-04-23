import pandas

class DatasetAnalyzer:
    def __init__(self, csv_file):
        self.dataframe = pandas.read_csv(csv_file)

    def question_one(self):
        print("""
            1.  Qual é a média de nota dos aprovados (no período total e por ano)?
        """)

        # remove all students with type 'EQUIVALENCIA' because they don't have grade
        approved_students = self.dataframe[(self.dataframe['status'] == 'Aprovado') & (self.dataframe['tipo'] != 'EQUIVALENCIA')]
        approved_students_mean = approved_students['nota'].mean()

        print(f"Média de nota dos aprovados (total): {approved_students_mean:.2f}")

        approved_students_mean_by_year = approved_students.groupby('ano')['nota'].mean().round(2)

        print("Média de nota dos aprovados por ano:")
        print(approved_students_mean_by_year)
        print("\n")
        
        
    def question_two(self):
        print("""
            2.  Qual é a média de nota dos reprovados por nota (período total e ano)?
        """)

        repproved_students = self.dataframe[self.dataframe['status'] == 'R-nota']
        repproved_students_mean = repproved_students['nota'].mean()

        print(f"Média de nota dos reprovados por nota (total): {repproved_students_mean:.2f}")

        repproved_students_mean_by_year = repproved_students.groupby('ano')['nota'].mean().round(2)

        print(f"Média de nota dos reprovados por nota por ano:")
        print(repproved_students_mean_by_year)
        print("\n")

        
        
    def question_three(self):
        # total number of students who failed by grade in relation to the total number of students who failed (total period and per year)
        print("""
            3.  Qual é a frequência dos reprovados por nota (período total e por ano)?
        """)

        failed_students = self.dataframe[self.dataframe['status'].isin(['R-nota', 'R-freq'])]
        total_failed_students = len(failed_students)
        percentage_failed_by_grade_total = (len(self.dataframe[self.dataframe['status'] == 'R-nota']) / total_failed_students) * 100

        print(f"Porcentagem de alunos reprovados por nota (em relação aos que reprovaram - total): {percentage_failed_by_grade_total:.2f}%")

        failed_students_by_year = failed_students.groupby('ano')
        percentage_failed_by_grade_year = failed_students_by_year['status'].apply(lambda x: len(x[x == 'R-nota']) / len(x)) * 100
        percentage_failed_by_grade_year = percentage_failed_by_grade_year.round(2).apply(lambda x: "{:.2f}%".format(x))

        print(f"Porcentagem de alunos reprovados por nota (em relação aos que reprovaram - por ano):")
        print(percentage_failed_by_grade_year)
        print("\n")
        
        
    def question_four(self):
        print("""
            4.  Qual a porcentagem de evasões (total e anual)?
        """)
        
        total_records = len(self.dataframe)
        cancellations = self.dataframe[self.dataframe['status'].isin(['Cancelado', 'R-freq'])]
        total_cancellations = len(cancellations)
        percentage_total_cancellations = (total_cancellations / total_records) * 100
        print("Porcentagem de evasões no total: {:.2f}%".format(percentage_total_cancellations))

        cancellations_by_year = cancellations.groupby('ano').size()
        total_by_year = self.dataframe.groupby('ano').size()
        percentages_by_year = (cancellations_by_year / total_by_year) * 100
        formatted_percentages_by_year = percentages_by_year.apply(lambda x: "{:.2f}%".format(x) if not pandas.isna(x) else "0%")

        print("Porcentagem de evasões por ano:")
        print(formatted_percentages_by_year)
        print("\n")
        
        
    def question_five(self):
        print("""
            5.  Como os anos de pandemia impactaram no rendimento dos estudantes em 
                relação aos anos anteriores, considerando o rendimento dos aprovados, a taxa 
                de cancelamento e as reprovações? Considere como anos de pandemia 
                os anos de 2020 e 2021.
            """)

        pandemic_years = [2020, 2021]
        previous_years = self.dataframe[~self.dataframe['ano'].isin(pandemic_years)]
        pandemic_approved_avg = self.dataframe[(self.dataframe['ano'].isin(pandemic_years)) & (self.dataframe['status'] == 'Aprovado')]['nota'].mean()
        previous_approved_avg = previous_years[previous_years['status'] == 'Aprovado']['nota'].mean()

        pandemic_cancel_rate = (self.dataframe[self.dataframe['ano'].isin(pandemic_years)]['status'].value_counts().get('Cancelado', 0) / len(self.dataframe[self.dataframe['ano'].isin(pandemic_years)])) * 100
        previous_cancel_rate = (previous_years['status'].value_counts().get('Cancelado', 0) / len(previous_years)) * 100

        pandemic_freq_failure_rate = (self.dataframe[self.dataframe['ano'].isin(pandemic_years)]['status'].value_counts().get('R-freq', 0) / len(self.dataframe[self.dataframe['ano'].isin(pandemic_years)])) * 100
        previous_freq_failure_rate = (previous_years['status'].value_counts().get('R-freq', 0) / len(previous_years)) * 100

        pandemic_grade_failure_rate = (self.dataframe[self.dataframe['ano'].isin(pandemic_years)]['status'].value_counts().get('R-nota', 0) / len(self.dataframe[self.dataframe['ano'].isin(pandemic_years)])) * 100
        previous_grade_failure_rate = (previous_years['status'].value_counts().get('R-nota', 0) / len(previous_years)) * 100

        print("Rendimento dos Aprovados:")
        print("Média das notas nos anos de pandemia:", round(pandemic_approved_avg, 2))
        print("Média das notas nos anos anteriores:", round(previous_approved_avg, 2))
        print("\nTaxa de Cancelamento:")
        print("Taxa de cancelamento nos anos de pandemia:", round(pandemic_cancel_rate, 2), "%")
        print("Taxa de cancelamento nos anos anteriores:", round(previous_cancel_rate, 2), "%")
        print("\nReprovações:")
        print("Taxa de reprovação por frequência nos anos de pandemia:", round(pandemic_freq_failure_rate, 2), "%")
        print("Taxa de reprovação por frequência nos anos anteriores:", round(previous_freq_failure_rate, 2), "%")
        print("Taxa de reprovação por nota nos anos de pandemia:", round(pandemic_grade_failure_rate, 2), "%")
        print("Taxa de reprovação por nota nos anos anteriores:", round(previous_grade_failure_rate, 2), "%")

        print("""
            Como podemos ver, a média das notas de alunos aprovados aumentou em anos de pandemia. 
            Porém, apesar disso, a taxa de cancelamento e reprovações são indicadores que foram 
            impactados negativamente.
            """)
        print("\n")

        
        
    def question_six(self):
        print("""
            6.  Compare a volta às aulas híbrida (2022 período 1) com os anos de 
                pandemia e os anos anteriores.
            """)

        hybrid_years = [2022]
        previous_years = self.dataframe[~self.dataframe['ano'].isin(hybrid_years)]
        hybrid_approved_avg = self.dataframe[(self.dataframe['ano'].isin(hybrid_years)) & (self.dataframe['status'] == 'Aprovado')]['nota'].mean()
        previous_approved_avg = previous_years[previous_years['status'] == 'Aprovado']['nota'].mean()

        hybrid_cancel_rate = (self.dataframe[self.dataframe['ano'].isin(hybrid_years)]['status'].value_counts().get('Cancelado', 0) / len(self.dataframe[self.dataframe['ano'].isin(hybrid_years)])) * 100
        previous_cancel_rate = (previous_years['status'].value_counts().get('Cancelado', 0) / len(previous_years)) * 100

        hybrid_freq_failure_rate = (self.dataframe[self.dataframe['ano'].isin(hybrid_years)]['status'].value_counts().get('R-freq', 0) / len(self.dataframe[self.dataframe['ano'].isin(hybrid_years)])) * 100
        previous_freq_failure_rate = (previous_years['status'].value_counts().get('R-freq', 0) / len(previous_years)) * 100

        hybrid_grade_failure_rate = (self.dataframe[self.dataframe['ano'].isin(hybrid_years)]['status'].value_counts().get('R-nota', 0) / len(self.dataframe[self.dataframe['ano'].isin(hybrid_years)])) * 100
        previous_grade_failure_rate = (previous_years['status'].value_counts().get('R-nota', 0) / len(previous_years)) * 100

        print("Rendimento dos Aprovados:")
        print("Média das notas no ano híbrido:", round(hybrid_approved_avg, 2))
        print("Média das notas nos anos anteriores:", round(previous_approved_avg, 2))
        print("\nTaxa de Cancelamento:")
        print("Taxa de cancelamento no ano híbrido:", round(hybrid_cancel_rate, 2), "%")
        print("Taxa de cancelamento nos anos anteriores:", round(previous_cancel_rate, 2), "%")
        print("\nReprovações:")
        print("Taxa de reprovação por frequência no ano híbrido:", round(hybrid_freq_failure_rate, 2), "%")
        print("Taxa de reprovação por frequência nos anos anteriores:", round(previous_freq_failure_rate, 2), "%")
        print("Taxa de reprovação por nota no ano híbrido:", round(hybrid_grade_failure_rate, 2), "%")
        print("Taxa de reprovação por nota nos anos anteriores:", round(previous_grade_failure_rate, 2), "%")

        print("""
            O ano de volta as aulas, no modelo híbrido, foi um momento de transição, 
            onde podemos ver que as taxa de cancelamentos e reprovações se manteve estável, 
            porém, houve um aumento significativo na média de nota dos aprovados.
        """)
        print("\n")
        
    def question_seven(self):
        print("""
            7.  Compare a volta às aulas presencial (2022 período 2) com a volta 
                híbrida do item anterior.
            """)

        print("""
            Não é possível fazer essa comparação, pois os registros do ano 2022 - período 2 
            se referem a matriculas em andamento, ou seja, não possuem nota e frequência no dataset.
        """)
       

# instantiate the DatasetAnalyzer class with the CSV file
analyzer = DatasetAnalyzer('historico-alg1_SIGA_ANONIMIZADO.csv')

analyzer.question_one()
analyzer.question_two()
analyzer.question_three()
analyzer.question_four()
analyzer.question_five()
analyzer.question_six()
analyzer.question_seven()
