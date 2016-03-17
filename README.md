# TnT based Part of Speech Tagger for Hindi

## Making the model:
- Run: python tnt_tagger.py train-file test-file
- e.g: python tnt_tagger.py train.hin test.hin
- Note: test file is not needed

## Tagging Sentences:
- Run: python tagger.py file-with-sentences output-format
- output-format:
	- terminal : for output to stdout
        - file-name: for output to a file
  e.g:  
	- python tagger.py check.txt terminal
        - python tagger.py check.txt output.txt


## Accuracy:
   The tagger gives 84% accuracy for 
   20000 lines of training data 
   5000 lines of testing data
