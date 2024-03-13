# subword-miniproject-2
Mini-Project 2 for 11824. I improve upon two baseline methods (neural and non-neural) for paradigm completion and reinflection for 3 languages - Kabardian (kbd), Swahili (swc), and Mixtec (xty).
 ## File Structure
The files are organized as follows:
- dataset:- Contains the given train/test/dev files as well as the augmented files and preprocessed train files.
- 1_Scripts:- Cotains the scripts used for data preparation, augmentation and training the model as well as inferencing to produce the final inflected forms.
- 2_Final_Submission:- The predicted inflected forms for the lemmas and tags for the three languages.
- 3_Augment_Data - The extra data files I used to augment the training data for kbd and swc. All the files were obtained from the Sigmorphon 2019 Shared [Task 1](https://github.com/sigmorphon/2019/tree/master/task1) data directory.
  
 ## Run Commands
Navigate to the 'kbd' and 'swc' subfolders in 0_Scripts and simply run:-
`sbatch run.sh` \
For 'xty', further navigate to the 'neural-transducer' directory and run:-
`sbatch run_tagtransformer.sh`

 ## My Approach
### Kabardian (kbd) and Swahili (swc) ([code](https://github.com/Aadit3003/subword-miniproject-2/blob/01bd97a177a78948b1d2869e06f717b089a90014/1_Scripts/kbd/prep.py))
For these two languages, the neural baseline proved to be weaker than the non-neural baseline. I thought that augmenting it with data would be an easy way to drive up the accuracy metric. Swahili data was readily available (around 9000 more data points) as it was one of the high-resource languages for Sigmorphon 2019, while Kabardian data was more scarce (around 200 more data points). All these files can be found in the [3_Augment_Data](https://github.com/Aadit3003/subword-miniproject-2/tree/7cb88b6b033c25f0eae500cacc7203df5c133068/3_Augment_Data) folder above. I tried 3 approaches with data augmentation - First, simply concatenating the new data, this worked very well and surpassed both the baselines. Next, I tried a "self-pollination" approach by using cartesian products of lemmas and tags both from the new files. Finally, I tried a "cross-pollination" approach by augmenting the data with cartesian product pairs of lemmas from the new files, and tags, affixes from the existing train data. In both languages the simple addition worked better than self-pollination which in-turn worked better than cross-pollination. Kabardian showed slight improvement in the dev set performance (88.3 to 88.67), while Swahili showed a dramatic improvement (71.5 to 95.9). The results can be seen here:
- [Kabardian](https://github.com/Aadit3003/subword-miniproject-2/blob/417d7239c8755cb9dfcf617c26e3bd777cc508fb/1_Scripts/kbd/kbd.out)
- [Swahili](https://github.com/Aadit3003/subword-miniproject-2/blob/7cb88b6b033c25f0eae500cacc7203df5c133068/1_Scripts/swc/swc.out)

### Mixtec ([code](https://github.com/Aadit3003/subword-miniproject-2/blob/6d43ab126a32b8106f42604d1a5ec6c48629de15/1_Scripts/xty/neural-transducer/run_tagtransformer.sh))
Since I could not find high-quality data for augmentation with Mixtec, and the neural baseline was giving good results, I decided to play around with hyperparameter optimization. I did a grid search by varying the following hyperparameters:
- layers = [4, 8, 10]
- architecture = [hmm, hmmfull, tagtransformer, taguniversaltransformer]
- decode = [greedy, beam]
- attention_heads = [4, 8]

I found that the tagtransformer was giving me the best dev set [results](https://github.com/Aadit3003/subword-miniproject-2/blob/6d43ab126a32b8106f42604d1a5ec6c48629de15/1_Scripts/xty/neural-transducer/tag.out) with 10 layers, 4 attention heads and greedy decoding (80.16 on the dev set), closely followed by the taguniversaltransformer [results](https://github.com/Aadit3003/subword-miniproject-2/blob/6d43ab126a32b8106f42604d1a5ec6c48629de15/1_Scripts/xty/neural-transducer/universal.out) (79.36). I had to use "PLACEHOLDER" tokens in the test case files, since there was no gold labeling, and hence could not report the test set metrics.
