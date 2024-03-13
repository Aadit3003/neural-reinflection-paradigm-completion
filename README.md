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
### Kabardian (kbd) and Swahili (swc) [code](https://github.com/Aadit3003/subword-miniproject-2/blob/01bd97a177a78948b1d2869e06f717b089a90014/1_Scripts/kbd/prep.py)
For these two languages, the neural baseline proved to be weaker than the non-neural baseline. I thought that augmenting it with data would be an easy way to drive up the accuracy metric. Swahili data was readily available (around 9000 more data points) as it was one of the high-resource languages for Sigmorphon 2019, while Kabardian data was more scarce (around 200 more data points). All these files can be found in the 3_Augment_Data folder above. I tried 3 approaches with data augmentation - First, simply concatenating the new data, this worked very well and surpassed both the baselines. Next, I tried a "self-pollination" approach by using cartesian products of lemmas and tags both from the new files. Finally, I tried a "cross-pollination" approach by augmenting the data with cartesian product pairs of lemmas from the new files, and tags, affixes from the existing train data. In both languages the simple addition worked better than self-pollination which in-turn worked better than cross-pollination. Kabardian showed slight improvement in the dev set performance (88.3 to 88.67), while Swahili showed a dramatic improvement from 71.5 to 95.9. The results can be seen here:
- [kbd]([https://github.com/Aadit3003/subword-miniproject-2/blob/417d7239c8755cb9dfcf617c26e3bd777cc508fb/1_Scripts/kbd/kbd.out])
- b

### Mixtec ([code](https://github.com/Aadit3003/subword-miniproject-1/blob/7dd2aca9aecd7bf9b28f99a1d81c56613a8b4cd4/0_Scripts/tokenizer_SHP_Morfessor_Flatcat.py))
Building on the baseline code provided for Morfessor, I trained a baseline Morfessor model (recursive algorithm) on the train set and performed segmentation using the baseline model. I added this corpus of the baseline segmented data to a Flatcat model and initialized its Hidden Markov Model. This was followed by using the viterbi segment method and evaluation. The improvements over the baseline Morfessor were not too significant, but it beat the baselines.

I experimented with using the "force_split" and "no_split" parameters by observing morphemes in the train and dev target files and populating these lists. I included some common character pairs that appeared at morpheme boundaries to the force_split list (for both the Morfessor baseline and Flatcat models). Similarly, I added character pairs that always occurred internal to the morphemes to the no_split list. This seemed to improve performance slightly, however, adding too many character pairs severely degraded the performance.
