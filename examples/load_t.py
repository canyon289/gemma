
import sentencepiece as spm

path_tokenizer = "/home/canyon/repos/gemma/tokenizer.model"

vocab = spm.SentencePieceProcessor()
vocab.Load(path_tokenizer)