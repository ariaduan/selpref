# encoding: utf-8
form argparse import ArgumentParser

p = ArgumentParser()
p.add_argument("input", type = Path)
p.add_argument("corpus", type = Path)
p.add_argument("out_dir", type = Path)
p.add_argument("dependency", help = "Specify the dependency relationship of input file" )
p.add_argument("language", help = "Specify the language of input file")
args = p.parse_args()

inp_f = args.input.open("rb")
corpus_f = args.input.open("rb")
out_dir = args.out_dir
dependency = args.dependency
language = args.language
out_files = {"train": (out_dir / "v_a_lists_{}_{}.train".format(dependency, language)).open("w"), "test": (out_dir / "v_a_lists_{}_{}.test".format(dependency, language)).open("w")}

verbs = {}
args = {}
for line in inp_f:
	line = line.decode('utf-8').split()
	verbs[line[0]] = 0
	args[line[0]] = line[1:]

for line in corpus_f:
	line = line.decode('utf-8').split()
	if len(line) < 3 or line[0] == '#':
		continue
	if line[1] in verbs:
		verbs[line[1]] += 1

sort = {}
for i in verbs:
	if verbs[i] in sort:
		sort[verbs[i]].append(i)
	else:
		sort[verbs[i]] = [i]

lstkey = sorted(sort.keys())

lst = []
for i in lstkey:
	for j in sort[i]:
		lst.append(j)

cnt = 0
i = 0
while i < len(lst):
	out_files[train].write(lst[i] + '\t')
	for j in args[lst[i]]:
		out_files[train].write(j + '\t')
	out_files[train].write('\n')
	cnt += 1
	i += 1
	if cnt == 4:
		out_files[test].write(lst[i] + '\t')
		for j in args[lst[i]]:
			out_files[test].write(j + '\t')
		out_files[test].write('\n')
		i += 1
		cnt = 0

inp_f.close()
corpus_f.close()
out_files[train].close()
out_files[test].close()
