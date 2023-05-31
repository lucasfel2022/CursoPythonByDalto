otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Diferencias con otros cursos

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max =  100 - dalto_curso * 1000 // otros_cursos_max/ 10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

print(f"La diferencia con minima es de: {diferencia_con_min}")
print(f"La diferencia con maxima es de: {diferencia_con_max}")
print(f"La diferencia con el promedio es de: {diferencia_con_promedio}")

