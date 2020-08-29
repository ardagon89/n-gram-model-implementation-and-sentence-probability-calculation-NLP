Execute: python Bigram.py <filename <smoothing_code>>

- Both filename and smoothing_code are optional parameters and can be omitted. In that case the input filename is hardcoded in the program.
- If filename is passed as argument to the program the file should be in the same folder as the Bigram.py file.
- If smoothing_code is passed along with the filename as an argument to the program, then only NS, LS and GTS are the valid values for smoothing_code.

smoothing_code can take the following values:
NS : No smoothing
LS : Laplace smoothing
GTS : Good Turing smoothing

----------------------------------------------------------------------------------------------------------------------------------------
Example 1: python Bigram.py

Output : 

the:0.053479203340267976
('the', 'standard'):0.0008161044613710555
('standard', 'turbo'):0.2
('turbo', 'engine'):0
('engine', 'is'):0
('is', 'hard'):0
('hard', 'to'):0.75
('to', 'work'):0.004513217279174726

No smoothed prob: 0.0

the:0.053479203340267976
('the', 'standard'):0.0003546728143287817
('standard', 'turbo'):0.00039411455596426696
('turbo', 'engine'):0.0001315097317201473
('engine', 'is'):0.000131250820317627
('is', 'hard'):0.00012423903590508137
('hard', 'to'):0.0005259006047856955
('to', 'work'):0.0008740303725554463

Laplace smoothed prob: 7.368574707097542e-27

the:0.053479203340267976
('the', 'standard'):4.520905085529811e-05
('standard', 'turbo'):1.2824430746649818e-05
('turbo', 'engine'):0.2483575627283251
('engine', 'is'):0.2483575627283251
('is', 'hard'):0.2483575627283251
('hard', 'to'):4.520905085529811e-05
('to', 'work'):0.00010794966406900566

Good Turing prob: 2.3180738471938815e-21

----------------------------------------------------------------------------------------------------------------------------------------
Example 2: python Bigram.py NLP6320_POSTaggedTrainingSet-Windows.txt

Output :

the:0.053479203340267976
('the', 'standard'):0.0008161044613710555
('standard', 'turbo'):0.2
('turbo', 'engine'):0
('engine', 'is'):0
('is', 'hard'):0
('hard', 'to'):0.75
('to', 'work'):0.004513217279174726

No smoothed prob: 0.0

the:0.053479203340267976
('the', 'standard'):0.0003546728143287817
('standard', 'turbo'):0.00039411455596426696
('turbo', 'engine'):0.0001315097317201473
('engine', 'is'):0.000131250820317627
('is', 'hard'):0.00012423903590508137
('hard', 'to'):0.0005259006047856955
('to', 'work'):0.0008740303725554463

Laplace smoothed prob: 7.368574707097542e-27

the:0.053479203340267976
('the', 'standard'):4.520905085529811e-05
('standard', 'turbo'):1.2824430746649818e-05
('turbo', 'engine'):0.2483575627283251
('engine', 'is'):0.2483575627283251
('is', 'hard'):0.2483575627283251
('hard', 'to'):4.520905085529811e-05
('to', 'work'):0.00010794966406900566

Good Turing prob: 2.3180738471938815e-21
----------------------------------------------------------------------------------------------------------------------------------------
Example 3: python Bigram.py NLP6320_POSTaggedTrainingSet-Windows.txt NS

Output :

the:0.053479203340267976
('the', 'standard'):0.0008161044613710555
('standard', 'turbo'):0.2
('turbo', 'engine'):0
('engine', 'is'):0
('is', 'hard'):0
('hard', 'to'):0.75
('to', 'work'):0.004513217279174726

No smoothed prob: 0.0
----------------------------------------------------------------------------------------------------------------------------------------
Example 4: python Bigram.py NLP6320_POSTaggedTrainingSet-Windows.txt LS

Output :

the:0.053479203340267976
('the', 'standard'):0.0003546728143287817
('standard', 'turbo'):0.00039411455596426696
('turbo', 'engine'):0.0001315097317201473
('engine', 'is'):0.000131250820317627
('is', 'hard'):0.00012423903590508137
('hard', 'to'):0.0005259006047856955
('to', 'work'):0.0008740303725554463

Laplace smoothed prob: 7.368574707097542e-27
----------------------------------------------------------------------------------------------------------------------------------------
Example 5: python Bigram.py NLP6320_POSTaggedTrainingSet-Windows.txt GTS

Output :

the:0.053479203340267976
('the', 'standard'):4.520905085529811e-05
('standard', 'turbo'):1.2824430746649818e-05
('turbo', 'engine'):0.2483575627283251
('engine', 'is'):0.2483575627283251
('is', 'hard'):0.2483575627283251
('hard', 'to'):4.520905085529811e-05
('to', 'work'):0.00010794966406900566

Good Turing prob: 2.3180738471938815e-21
----------------------------------------------------------------------------------------------------------------------------------------
Example 6: python Bigram.py NLP6320_POSTaggedTrainingSet-Windows.txt X

Output :

Wrong input. Enter correct smoothing code.
----------------------------------------------------------------------------------------------------------------------------------------
Example 7: python Bigram.py NLP6320_POSTaggedTrainingSet-Windows.txt X Y

Output :

Wrong number of arguments provided.
----------------------------------------------------------------------------------------------------------------------------------------