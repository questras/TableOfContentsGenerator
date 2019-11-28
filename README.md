# TableOfContentsGenerator
Script that generates table of contents based on headers in markdown language text.  
Script deletes previous table of content and creates new one according to file.  


## Usage:  
Run the script specifying input file path and (optionally) output file path.

```
python3 generator.py -i <input_file_path> -o <optional_output_file_path>
```

Not specyfing the output file path will result in overriding input file, so be careful.

**Example**
```
# generate table of contents and override input file
python3 generator.py -i README.md

# generate table of contents and save the output as output file
python3 generator.py -i README.md -o README2.md
```
