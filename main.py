# FASTA Reader & Analyzer

# Open FASTA file
with open ("sample.fasta","r") as fasta_file:
    lines = fasta_file.readlines()

# Extract header
header = lines[0].strip()

# Join all DNA sequence lines
dna = ""

for line in lines[1:]:
    dna += line.strip()

# Display information
print("Header:", header)
print("DNA Sequence:", dna)
print("Sequence Length:", len(dna))

# Nucleotide Count
print("\nNucleotide Count")
print("A:", dna.count("A"))
print("T:", dna.count("T"))
print("G:", dna.count("G"))
print("C:", dna.count("C"))

# GC Content
gc = dna.count("G") + dna.count("C")
gc_content = (gc / len(dna)) * 100

print(f"\nGC Content: {gc_content:.2f}%")

# DNA → RNA
rna = dna.replace("T", "U")
print("\nRNA Sequence:", rna)

# Reverse Complement
complement = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}

reverse_complement = ""

for base in dna:
    reverse_complement += complement[base]

reverse_complement = reverse_complement[::-1]

print("\nReverse Complement:", reverse_complement)