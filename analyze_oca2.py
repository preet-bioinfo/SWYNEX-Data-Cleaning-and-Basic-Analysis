from collections import Counter
import csv

# Read the FASTA file
with open("OCA2-mRNA.fasta", "r") as file:
    lines = file.readlines()

# Extract and clean the sequence
sequence = "".join(
    line.strip() for line in lines
    if not line.startswith(">")
).upper()

# Basic analysis
counts = Counter(sequence)
valid_bases = "ATGC"
invalid = [base for base in sequence if base not in valid_bases]
gc_content = (
    (counts["G"] + counts["C"]) / len(sequence) * 100
    if sequence else 0
)

print("OCA2 mRNA Sequence Analysis")
print("Sequence length:", len(sequence))
print("A:", counts["A"])
print("T:", counts["T"])
print("G:", counts["G"])
print("C:", counts["C"])
print(f"GC content: {gc_content:.2f}%")
print("Invalid characters:", len(invalid))

# Save results to CSV
with open("oca2_analysis.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Metric", "Value"])
    writer.writerow(["Sequence length", len(sequence)])
    writer.writerow(["A count", counts["A"]])
    writer.writerow(["T count", counts["T"]])
    writer.writerow(["G count", counts["G"]])
    writer.writerow(["C count", counts["C"]])
    writer.writerow(["GC content (%)", round(gc_content, 2)])
    writer.writerow(["Invalid characters", len(invalid)])

print("Results saved to oca2_analysis.csv")