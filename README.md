# NLP Experiment
GOal: After being trained on Markdown files from a local folder (say Handbook) and create a chat interface to be able to get answers to user's quetions.

## Steps
_With inputs from GPT-4_

- **Preprocess the Data**: Parse your markdown files to extract the content (Using `markdown` and `BeautifulSoup`) ✅
- **Format the Data**: BERT requires data in a specific format. Each document should be split into sentences or segments, which are then tokenized (split into individual words or subwords).
-   The Transformers library by Hugging Face provides tools for tokenizing text data in the way that BERT requires.
- **Create Training and Validation Sets**: Split your data into training and validation sets. The training set is used to train the model, while the validation set is used to evaluate the model's performance during and after training.
- **Train the Model**: Use the Transformers library to load a pre-trained BERT model and fine-tune it on your data. You'll need to define a training loop that feeds your tokenized text data into the model, calculates the loss, and updates the model's weights.
- **Evaluate and Test the Model**: After training, evaluate the model's performance on your validation set. Check the loss and any other metrics you're interested in (such as accuracy, if you have labels for your data). You can then test the model by giving it new, unseen questions and see how well it generates appropriate responses.
- **Iterate**: Based on your evaluation, you may need to adjust your training process, tweak the model's parameters, or preprocess your data differently.
- **Chat interface**: Add a chat interface for a user to be able to input their query and get responses back (with citation links).
