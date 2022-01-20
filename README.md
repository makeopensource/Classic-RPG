# Classic-RPG
A classic role playing game with homemade engine.
## Set Up
For this project we will be using Open-JDK 17 (As this is the most recent stable release of JDK) Be sure you have the proper version installed.
## Design Doc:
Has now been moved to the wiki tab for version control. Check out the wiki tab above!
## Pulling from a fork:
Set upstream:  
git remote add upstream git@github.com:makeopensource/Classic-RPG.git  
(if this does not work, you're likely using https instead of ssh, try "git remote add upstream https://github.com/makeopensource/Classic-RPG.git")  
Fetch:  
git fetch  
Pull upstream:  
git pull upstream <branchname> (Most likely will be dev.)
## Creating Tests:
To quickly create tests for a class, right-click on the class name in intellij, click show context actions, and then click create test.  
Place the tests in an appropriately formatted folder.