### Kladde Lab Scripts
A collection of scripts for processing NGS epigentic data.

rename_header.py  -- Renames the header of alignment fasta files from bsDraw.py output.\
get_lengths.py  -- Script to get the lengths of ccs reads, fasta reads, alignments and references.\
filter_fasta.py -- Filters alignments from fasta that don't meet user supplied parameters.\
make_corr_plots.py  -- Generates scatterplots with regression line for replicates of NGC data.\
get_NFR_cuts.py -- Determines freguency of potentially truncated NFRs in record.tsv file from rrbs.py output.\
annotateFiles.py  -- Processes the output Excel files from the atacseq pipeline and from DMAP2/metilene pipeline. Generates detailed genomic feature annotations and reformatting of data.


### USAGE:

#### rename_header.py
usage: rename_header.py [-h] names_file dir_name

Run rename_header.py -h for help. Renames fasta header from fasta files generated by bsDraw. This is necessary when using these files with rrbs.py. Provide a file, in bed-like format with the coordinates of fragment, and the old and new header names. This usually made by modifying the report file from fastools digest. (tsv format with chr, start, end, fragment_ID, length, new_ID).

positional arguments:
  names_file  bed-like file containing the reference fragment coords plus old
              and new names.
  dir_name    directory to read files from.

optional arguments:
  -h, --help  show this help message and exit

#### get_lengths.py
usage: get_lengths.py [-h] [dir_name] mode

Run get_fasta_lengths.py -h for help.For 'alignment' and 'ccs' modes, this script will generate the lengths of aligned reads from an alignment fasta generated by bsDraw.py or the lengths of ccs reads. In 'fasta' mode, this will print to the screen the gene/fragment name, reference length, max alignment length, min alignment length and the difference between the max and min lengths. This is useful for trouble shooting or determining if filtering of alignments should be done.

positional arguments:
  dir_name    Directory containing the .fa files to be analyzed.
  mode        Mode to run in. Options are 'alignment', 'ccs', and 'fasta'.

optional arguments:
  -h, --help  show this help message and exit
  
 #### filter_fasta.py
 usage: filter_fasta.py [-h] [-o OUTPUT] filename percent

Filter an alignment fasta (produced by bsDraw) by percentage of max aligned read length

positional arguments:
  filename              Input fasta file to be filtered
  percent               Percent

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Specify an optional output file name

#### make_corr_plots.py
usage: make_corr_plots.py [-h] dir1_name dir2_name site

This script will generate correlation plots for each gene/fragment between replicates using the output of methylmapper (.freqs.csv files). Typically used for finding correlation of NGC replicates. When calling this script, provide the path to each replicate's directory and the site you are interested in (e.g. HCG). This will generate a scatter plot for each gene/fragment with a regression line and r-squared and a three column table with site position and site frequency. It also generates a plot and table for the combined data for every gene/fragment in the directories.

positional arguments:
  dir1_name   Directory containing the first replicate
  dir2_name   Directory containing the second replicate
  site        Specifies what frequency table site to read. Should be either
              HCG or GCH.

optional arguments:
  -h, --help  show this help message and exit

#### get_NFR_cuts.py
usage: get_NFRs_cuts.py [-h] filename outfile minlength

This program determines which NFRs are potentially cut by BsaWI sites. This reads the records file from rrbs.py and gives as output a file with all cut sites and the patch lengths, positions (5', 3' or both) and coordinates, as well as the fragment length and IDs of fragment and read. Also prints out to the screen the total number of NFRs analyzed and the number of cuts at each location and the percentage of cut

positional arguments:
  filename    Name of the records.tsv file to be analyzed
  outfile     Name of output file
  minlength   Minimum length of NFR to be counted

optional arguments:
  -h, --help  show this help message and exit

#### annotateFiles.py
usage: annotateFiles.py [-h] [-f FILE_PREFIX] dir_name mode

To Run, call this program and give the directory containing the input files and the prefix of the input file names as arguments.This script will annotate the ATAC-Seq differential analysis output files of dasa (part of the atacseq pipeline). These will be in excel (.xlsx) format and have two spreadsheets per workbook. This will format the Excel files and submit them to HOMER for annotation. It then combines the annotated files with the original data (i.e. peak data), and outputs an excel workbook with a sheet for each contrast.

positional arguments:
  dir_name              Directory containing the input excel (.xlsx) files
  mode                  Mode to run annotation in. Use atacseq to process the
                        atacseq (dasa) output exel files. Use metilene to
                        process the Metilene output excel files.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE_PREFIX, --file_prefix FILE_PREFIX
                        Optional filename prefix. Only use when mode is
                        atacseq. For example, for M-Series data, use M as the
                        prefix.
