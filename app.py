import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Nome": ["Ana", "Pedro"],
    "Idade": [22, 23],
})

print(df)

# DataFrame -- Estruturas de dados tabulares com colunas de diferentes tipos
# Series -- Estruturas de dados unidimensional que podem conter qualquer tipo de dado

series = pd.Series(
    [22, 23], index=["Ana", "Pedro"],
    name="idade"
)

print("\n\n", series)



# numpy -- Estruturas de dados eficientes para operações matemáticas

arr = np.array([1,2,3])
print("\n\n", arr)
