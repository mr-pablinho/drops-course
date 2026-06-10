Generate quiz questions for a lesson in the drops-course project, formatted for the jupyterquiz library.

The user provides a file path: /quiz-generator book/04-classical-ml/03-random-forests.ipynb

---

## Steps

1. Read the lesson notebook at the provided path.

2. Identify the 5–8 most important concepts, definitions, formulas, or procedures in the lesson. Ignore code syntax; focus on concepts a hydrologist should retain.

3. For each concept, generate one question. Mix question types:
   - **MCQ** (multiple choice): 1 correct answer + 3 plausible distractors
   - **True/False**: a claim that is definitively true or false (avoid "it depends" situations)
   - **What would happen if...**: test understanding of a consequence

4. Rules for good distractors:
   - Each distractor should be something a confused reader might actually believe
   - No distractor should be a valid alternative correct answer
   - Avoid "all of the above" / "none of the above"
   - Avoid distractors that are obviously absurd

5. Write the output in two formats:

**Format A — jupyterquiz JSON** (for embedding in the notebook):
```json
[
  {
    "question": "What does a Nash-Sutcliffe Efficiency (NSE) of 1.0 indicate?",
    "type": "many_choice",
    "answers": [
      {"answer": "The model perfectly reproduces the observed hydrograph.", "correct": true, "feedback": "Correct. NSE = 1 means zero residual variance."},
      {"answer": "The model performs as well as using the observed mean as a benchmark.", "correct": false, "feedback": "That describes NSE = 0, not NSE = 1."},
      {"answer": "The model explains 100% of the variance in precipitation.", "correct": false, "feedback": "NSE measures streamflow simulation skill, not precipitation."},
      {"answer": "The model has no bias.", "correct": false, "feedback": "NSE can equal 1 even with systematic bias if peak timing is perfect — use PBIAS separately."}
    ]
  }
]
```

**Format B — Notebook cell** (ready to paste into the quiz lesson):
```python
from jupyterquiz import display_quiz
display_quiz("quiz_module_N.json")
```
Also emit the JSON as a string that can be saved to `quiz_module_N.json`.

6. After generating the questions, flag any that need manual verification:
   ```
   REVIEW NEEDED:
   - Q3: The distractor "SPEI includes evapotranspiration, SPI does not" is correct — this makes it a valid answer, not a distractor. Revise.
   ```

7. Remind the user:
   "These questions are DRAFTS. Run /content-reviewer on the quiz file before merging — auto-generated distractors are where scientific errors most commonly appear."
