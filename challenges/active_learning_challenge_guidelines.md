# Guidelines for active learning exercises:

In general, we want these exercises to feel **'relevant'** to students, so they can really see how the foundational concepts they're learning in python or at the command line apply in work settings.

In the past, examples based on things like creating mock 'user accounts' for twitter or bank accounts, working with Spotify songs and artist information, pieces of develping websites, or data related to covid-19 have seemed to resonate with students to show them that they can use their coding skills to solve real-world tasks.

In general, we're hoping to set up these exercises so that students can work on them in groups of 4-5 with an instructor, or possibly in pairs, in breakout rooms.

### Exercise format

* Should take students about 1 hour to complete
* Should have a **challenge description file written as a markdown document** with instructions for what students should do
* Should include a completed solution (in fact the initial draft can include the solutions, then we can remove this before giving to students)
* If the exercise requires multiple files, they should all be contained in 1 directory (including the challenge description markdown)
* Students should be able to complete the challenge just through writing code with a text editor (atom, sublime, etc) and running scripts from the command line


### Suggestions:
* Exercises that come with some code already written are best! There are a couple ways we can do this
  * Give students scripts with missing parts and clear markings of what they need to fill in
  * Give students 2 scripts:
    * One script of helper functions
    * One script that imports the helper functions script at the top, then is blank for students to fill in / run to complete the exercise
  * Give students a script that is complete, but with bugs or missing documentation. Then the assignment would be to debug / document the code
* In any exercise, if there is helper code that we have written that is beyond the scope of what students currently know, it should be **clearly separated** from the pieces students are writing. Either
  * In a separate script (ideal for longer/more complex code that we don't want them to worry about)
  * In separate functions that have clear indications that students don't need to edit them
* If some exercises ask students to install a library or two via `pip install` that's okay, but this should be well-documented in the markdown, and students shouldn't have to learn any new code to use the newly installed library.
* Eventually, we're hoping to have some of the active learning exercises build up into a larger 'project' over the course of the bootcamp. Not all exercises have to be part of this though
