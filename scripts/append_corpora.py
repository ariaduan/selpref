# encoding: utf-8
from argparse import ArgumentParser

p = ArgumentParser()
p.add_argument("inp_dir", type = Path) #.../UD_data
p.add_argument("out_dir", type = Path)
args = p.parse_args()

inp_dir = args.inp_dir()
out_dir = args.out_dir()

out_files = {"cs": (out_dir / "cs_UD").open("w"), "de": (out_dir / "de_UD").open("w"), "en": (out_dir / "en_UD").open("w"), "zh": (out_dir / "zh_UD").open("w")}

lst_cs =['CAC-master/cs_cac-ud-train','CAC-master/cs_cac-ud-test','CAC-master/cs_cac-ud-dev','CLTT-master/cs_cltt-ud-train','CLTT-master/cs_cltt-ud-test','CLTT-master/cs_cltt-ud-dev','FicTree-master/cs_fictree-ud-train','FicTree-master/cs_fictree-ud-test','FicTree-master/cs_fictree-ud-dev','PDT-master/cs_pdt-ud-train-c','PDT-master/cs_pdt-ud-train-l','PDT-master/cs_pdt-ud-train-m','PDT-master/cs_pdt-ud-train-v','PDT-master/cs_pdt-ud-test','PDT-master/cs_pdt-ud-dev','PUD-master/cs_pud-ud-test']
lst_de = ['GSD-master/de_gsd-ud-train','GSD-master/de_gsd-ud-test','GSD-master/de_gsd-ud-dev']
lst_en = ['EWT-master/en_ewt-ud-train','EWT-master/en_ewt-ud-test','EWT-master/en_ewt-ud-dev','GUM-master/en_gum-ud-train','GUM-master/en_gum-ud-test','GUM-master/en_gum-ud-dev','LinES-master/en_lines-ud-train','LinES-master/en_lines-ud-test','LinES-master/en_lines-ud-dev','ParTUT-master/en_partut-ud-train','ParTUT-master/en_partut-ud-test','ParTUT-master/en_partut-ud-dev','PUD-master/en_pud-ud-test']
lst_zh = ['CFL-master/zh_cfl-ud-test','GSD-master/zh_gsd-ud-train','GSD-master/zh_gsd-ud-test','GSD-master/zh_gsd-ud-dev','HK-master/zh_hk-ud-test','PUD-master/zh_pud-ud-test']
'''
out_files["cs"] = open('/Users/ariaduan1.0/Desktop/summer_experiment/Roger/projects/Jon/Selectional_preference/UD_data/cs_UD','w',encoding = 'utf-8')
out_files["de"] = open('/Users/ariaduan1.0/Desktop/summer_experiment/Roger/projects/Jon/Selectional_preference/UD_data/de_UD','w',encoding = 'utf-8')
out_files["en"] = open('/Users/ariaduan1.0/Desktop/summer_experiment/Roger/projects/Jon/Selectional_preference/UD_data/en_UD','w',encoding = 'utf-8')
out_files["zh"] = open('/Users/ariaduan1.0/Desktop/summer_experiment/Roger/projects/Jon/Selectional_preference/UD_data/zh_UD','w',encoding = 'utf-8')
'''
for i in lst_cs:
	name = inp_dir / "cs/UD_Czech-" + i + ".conllu"
	file = open(name, 'rb')
	for line in file:
		line = line.decode('utf-8')
		out_files["cs"].write(line)
	file.close()

for i in lst_de:
	name = inp_dir / "de/UD_German-" + i + ".conllu"
	file = open(name, 'rb')
	for line in file:
		line = line.decode('utf-8')
		out_files["de"].write(line)
	file.close()

for i in lst_en:
	name = inp_dir / "en/UD_English-" + i + ".conllu"
	file = open(name, 'rb')
	for line in file:
		line = line.decode('utf-8')
		out_files["en"].write(line)
	file.close()

for i in lst_zh:
	name = inp_dir / "zh/UD_Chinese-" + i + ".conllu"
	file = open(name, 'rb')
	for line in file:
		line = line.decode('utf-8')
		out_files["zh"].write(line)
	file.close()

out_files["cs"].close()
out_files["de"].close()
out_files["en"].close()
out_files["zh"].close()
