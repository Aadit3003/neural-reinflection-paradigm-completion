# subword-miniproject-2
Mini-Project 2 for 11824. I improve upon two baseline methods (neural and non-neural) for paradigm completion and reinflection for 3 languages - Kabardian (kbd), Swahili (swc), and Mixtec (xty).
 ## File Structure
The files are organized as follows:
- dataset:- Contains the given train/test/dev files as well as the augmented files and preprocessed train files.
- 1_Scripts:- Cotains the scripts used for data preparation, augmentation and training the model as well as inferencing to produce the final inflected forms.
- 2_Final_Submission:- The predicted inflected forms for the lemmas and tags for the three languages.
- 3_Augment_Data - The extra data files I used to augment the training data for kbd and swc. All the files were obtained from the Sigmorphon 2019 Shared Task 1 data directory.
  
 ## Run Commands
Navigate to the 'kbd' and 'swc' subfolders in 0_Scripts and simply run:-
`sbatch run.sh` \
For 'xty', further navigate to the 'neural-transducer' directory and run:-
`sbatch run_tagtransformer.sh`

 ## My Approach
### Wordpiece Tokenization for Rarámuri (tar) ([code](https://github.com/Aadit3003/subword-miniproject-1/blob/7dd2aca9aecd7bf9b28f99a1d81c56613a8b4cd4/0_Scripts/tokenizer_TAR_Wordpiece.py))
I used the Wordpiece tokenization algorithm, particularly the BertTokenizerFast() implementation from Huggingface ('bert-base-cased') for this task. I also tried using the 'xlm-roberta' tokenizer based on Sentencepiece, but it consistently underperformed as compared to the BertTokenizer. I performed grid search hyperparameter tuning for the vocabulary size and batch size, finally deciding on a vocabulary size of 900, and a batch size of 128. The runtime was roughly 0.12 seconds, slightly longer than SentencePiece, but much shorter than Morfessor. For tar it outperformed both baselines by a relatively large margin. However, this algorithm didn't seem to work as well for shp.

### Morfessor Flatcat for Shipibo-Konibo (shp) ([code](https://github.com/Aadit3003/subword-miniproject-1/blob/7dd2aca9aecd7bf9b28f99a1d81c56613a8b4cd4/0_Scripts/tokenizer_SHP_Morfessor_Flatcat.py))
Building on the baseline code provided for Morfessor, I trained a baseline Morfessor model (recursive algorithm) on the train set and performed segmentation using the baseline model. I added this corpus of the baseline segmented data to a Flatcat model and initialized its Hidden Markov Model. This was followed by using the viterbi segment method and evaluation. The improvements over the baseline Morfessor were not too significant, but it beat the baselines.

I experimented with using the "force_split" and "no_split" parameters by observing morphemes in the train and dev target files and populating these lists. I included some common character pairs that appeared at morpheme boundaries to the force_split list (for both the Morfessor baseline and Flatcat models). Similarly, I added character pairs that always occurred internal to the morphemes to the no_split list. This seemed to improve performance slightly, however, adding too many character pairs severely degraded the performance.
