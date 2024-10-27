import json

file_names = [
    '/mnt/c/Users/luuqu/Documents/GitHub/knowledge-harvest-from-lms/results/human/1000tuples_top20prompts/vinai/phobert-large/business/prompts.json',
    '/mnt/c/Users/luuqu/Documents/GitHub/knowledge-harvest-from-lms/results/human/1000tuples_top20prompts/vinai/phobert-large/business/ent_tuples.json',
    
    # '/mnt/c/Users/luuqu/Documents/GitHub/knowledge-harvest-from-lms/results/human/1000tuples_top20prompts/vinai/phobert-large/help/prompts.json',
    # '/mnt/c/Users/luuqu/Documents/GitHub/knowledge-harvest-from-lms/results/human/1000tuples_top20prompts/vinai/phobert-large/help/ent_tuples.json',
    
    # '/mnt/c/Users/luuqu/Documents/GitHub/knowledge-harvest-from-lms/results/human/1000tuples_top20prompts/vinai/phobert-large/ingredient_for/prompts.json',
    # '/mnt/c/Users/luuqu/Documents/GitHub/knowledge-harvest-from-lms/results/human/1000tuples_top20prompts/vinai/phobert-large/ingredient_for/ent_tuples.json',
    
    # '/mnt/c/Users/luuqu/Documents/GitHub/knowledge-harvest-from-lms/results/human/1000tuples_top20prompts/vinai/phobert-large/representative_figure/prompts.json',
    # '/mnt/c/Users/luuqu/Documents/GitHub/knowledge-harvest-from-lms/results/human/1000tuples_top20prompts/vinai/phobert-large/representative_figure/ent_tuples.json',
    
    # '/mnt/c/Users/luuqu/Documents/GitHub/knowledge-harvest-from-lms/results/human/1000tuples_top20prompts/vinai/phobert-large/separated_by_the_ocean/prompts.json',
    # '/mnt/c/Users/luuqu/Documents/GitHub/knowledge-harvest-from-lms/results/human/1000tuples_top20prompts/vinai/phobert-large/separated_by_the_ocean/ent_tuples.json'
]

for file_name in file_names:
    data = {}
    with open(file_name, 'r') as file:
        data = json.load(file)

    with open(file_name, 'w', encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2, separators=(',', ': '))
