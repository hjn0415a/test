from Bio import Entrez
import collections

# Set email address (required by NCBI)

# Search query
search_query = "OpenMS"

# Set email address (required by NCBI)
Entrez.email = "your_email@domain.com"

# Search PubMed
handle = Entrez.esearch(db="pubmed", term=search_query, retmax=1000)
record = Entrez.read(handle)

# Get IDs of all matching publications
id_list = record["IdList"]

# Retrieve data for each publication
pub_dict = collections.defaultdict(list)
for pub_id in id_list:
    pub_handle = Entrez.esummary(db="pubmed", id=pub_id, retmode="xml")
    pub_record = Entrez.read(pub_handle)[0]
    pub_title = pub_record["Title"]
    pub_authors = ", ".join(pub_record["AuthorList"])
    pub_journal = pub_record["FullJournalName"]
    pub_year = pub_record["PubDate"].split()[0]
    pub_url = f"https://www.ncbi.nlm.nih.gov/pubmed/{pub_id}"
    pub_entry = (
        f"- {pub_authors}. *{pub_title}*. {pub_journal}. {pub_year}. [Link]({pub_url})"
    )
    pub_dict[pub_year].append(pub_entry)

# Write list of publications to markdown file
with open("content/en/publications.md", "w") as file:
    file.write(f"# List of OpenMS Publications\n\n")
    for key, value in pub_dict.items():
        file.write(f"## {key}\n")
        file.write("\n\n".join(value))
        file.write("\n***\n")
