Benchmarking
=============
Learn how to benchmark your prompts across all models.

Introduction
-------------
When comparing LLMs, there is a constant tradeoff to make between quality, cost and latency. Stronger models are (in general) slower and more expensive - and sometimes overkill for the task at hand. Complicating matters further, new models are released weekly, each claiming to be state-of-the-art.

Benchmarking on your data lets you see how each of the different models perform on your task.

You can compare how quality relates to cost and latency, with live stats pulled from our `runtime benchmarks <https://unify.ai/benchmarks>`_.

When new models come out, simply re-run the benchmark to see how they perform on your task.


Preparing your dataset
-----------------------
You should create a dataset which is representative of the task you want to evaluate.
You’ll need a list of prompts, optionally including a reference, ‘gold-standard’ answer. You’ll get a more accurate benchmark if you include reference answers.

The file should be in JSONL format, with one entry per line, as shown below.
```
{"prompt": "This is the first prompt", "ref_answer": "This is the first reference answer"}
{"prompt": "This is the second prompt", "ref_answer": "This is the second reference answer"}
```
Use at least 50 prompts to get the most accurate results.
Currently there is an upper limit of 500 prompts, for most tasks we don’t tend to see much extra detail past ~250.

Benchmarking your dataset
-------------------------
In `your dashboard <https://console.unify.ai/dashboard>`_, clicking :code:`Select benchmark` and then :code:`Benchmark your prompts` opens the interface to upload a dataset.

You’ll receive an email when the benchmark finishes, and you’ll be able to select the graph in your `dashboard <https://console.unify.ai/dashboard>'_.

The x-axis can be set to represent cost, time-to-first-token, or inter-token latency, and on either a linear or log scale.

How does it work?
^^^^^^^^^^^^^^^^^^
The current benchmarks use gpt4o-as-a-judge (cf. https://arxiv.org/abs/2306.05685), to evaluate the quality of each model’s responses.


