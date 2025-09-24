ribbon:dict = {
    'Russia':[9.100,9.400],
    'Bulgaria':[9.600, 9.400],
    'Italy':[9.200,9.500]
}
hoop:dict = {
    'Russia':[9.300,9.800],
    'Bulgaria':[9.550,9.750],
    'Italy':[9.450,9.350]
}
rope:dict = {
    'Russia':[9.600,9.000],
    'Bulgaria':[9.500,9.400],
    'Italy':[9.700,9.150]
}
tools_set:dict = {
    "ribbon":ribbon,
    "hoop":hoop,
    "rope":rope,
}

country:str = str(input())
tool:str = str(input())


scores:list = tools_set[tool][country]
total_score:float = sum(scores)

percentage_score_missing:float = ((20 - total_score) / 20) * 100

print(f'The team of {country} get {total_score:.3f} on {tool}.')
print(f'{percentage_score_missing:.2f}%')