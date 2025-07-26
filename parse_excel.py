import pandas as pd

excel_file = '/home/ubuntu/upload/930E-5-PlanodeManutençãoPreventiva-15.07.2025.xlsx'
df = pd.read_excel(excel_file, header=None)

checklists = {}
current_category = 'Geral'
current_periodicity = 'Não Definida'

for index, row in df.iterrows():
    # Identify Category
    if 'Manutenção Mecânica' in str(row[0]) or 'Manutenção Mecânica' in str(row[1]):
        current_category = 'Mecânica'
    elif 'HIDRÁULICO' in str(row[0]) or 'HIDRÁULICO' in str(row[1]):
        current_category = 'Hidráulica'
    elif 'ELÉTRICA' in str(row[0]) or 'ELÉTRICA' in str(row[1]):
        current_category = 'Elétrica'
    elif 'GERAL' in str(row[0]) or 'GERAL' in str(row[1]):
        current_category = 'Geral'

    # Identify Periodicity
    if 'Cada' in str(row[0]) and 'H' in str(row[0]):
        current_periodicity = str(row[0]).strip()
    elif 'Cada' in str(row[1]) and 'H' in str(row[1]):
        current_periodicity = str(row[1]).strip()
    elif 'Cada' in str(row[2]) and 'H' in str(row[2]):
        current_periodicity = str(row[2]).strip()

    # Identify Checklist Items
    # Assuming checklist items start with a code like A.01, B.01, etc.
    if isinstance(row[0], str) and len(row[0]) > 1 and row[0][1] == '.' and row[0][0].isalpha():
        item_code = row[0]
        item_periodicity = row[1]
        item_description = row[2]
        item_observation = row[6] if len(row) > 6 else ''

        if current_category not in checklists:
            checklists[current_category] = {}
        if current_periodicity not in checklists[current_category]:
            checklists[current_category][current_periodicity] = []

        checklists[current_category][current_periodicity].append({
            'code': item_code,
            'periodicity': item_periodicity,
            'description': item_description,
            'observation': item_observation
        })

# Salvar a estrutura dos checklists em um arquivo JSON para fácil acesso
import json
with open("/home/ubuntu/checklists_structure.json", "w", encoding="utf-8") as f:
    json.dump(checklists, f, ensure_ascii=False, indent=4)

print("Estrutura dos checklists salva em checklists_structure.json")


