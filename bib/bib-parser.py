#%%
import bibtexparser
import glob

#%%
bib_files = glob.glob("references-*.bib")

# %%
bibs = [bibtexparser.parse_file(bib_file) for bib_file in bib_files]

# %%
bib_keys = {entry for bib in bibs for entry in bib.entries_dict}

# %%
bib_combo = bibtexparser.Library()

# %%
for bib in bibs:
    for entry in bib.entries:
        if entry.key in bib_keys:
            bib_combo.add(entry)
            bib_keys.remove(entry.key)

# %%
print(len(bib_combo.failed_blocks))

# %%

bibtexparser.write_file("references.bib", bib_combo)

# %%
