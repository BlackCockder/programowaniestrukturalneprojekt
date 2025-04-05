degreelist = [[30, 1.5, 5],  # Pracownia informatyczna LAB
              [60, 2, 5],  # Fizyka ogólna 1 ĆW
              [30, 2, 4],  # Fizyka ogólna 1 WYK
              [30, 1, 3],  # Chemia ogólna 1 ĆW
              [60, 1, 3.5],  # Chemia ogólna 1 WYK
              [60, 2, 4.5],  # Analiza matematyczna 1 ĆW
              [30, 2, 3],  # Analiza matematyczna 1 WYK
              [45, 1.5, 4.5],  # Programowanie w pythonie 1 ĆW
              [30, 1.5, 4],  # Programowanie w pythonie 1 WYK
              [30, 2, 5],  # Komputerowe wspomaganie pracowni fizycznej ĆW
              [30, 2, 4],  # Fizyka ogólna 2 ĆW
              [30, 2, 4.5],  # Fizyka ogólna 2 WYK
              [60, 2, 3.5],  # Analiza matematyczna 2 ĆW
              [30, 2, 3],  # Analiza matematyczna 2 WYK
              [30, 2, 4.5],  # Algebra liniowa ĆW
              [30, 2, 3],  # Algebra liniowa WYK
              [30, 2, 3],  # Mechanika teoretyczna ĆW
              [30, 2, 3],  # Mechanika teoretyczna WYK
              [30, 2, 5],  # Laby 1
              [30, 2, 4],  # Fizyka ogólna 3 ĆW
              [30, 2, 4],  # Fizyka ogólna 3 WYK
              [30, 2, 4],  # Astronomia WYK
              [30, 2, 4],  # Analiza matematyczna 3 ĆW
              [30, 2, 4.5],  # Analiza matematyczna 3 WYK
              ]
total = 0
for degree in degreelist:
    total += degree[0] * degree[1] * (degree[2] - 2)
print(total / 30)
