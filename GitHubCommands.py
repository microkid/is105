 

    git status - see what the current state of our project is: 

    "untracked" - new file 

    git add "octocat.txt" - den valgte filen - Dette er for å legge filen inn i "staging area" for å følge med på endringene 

Staging Area: A place where we can group files together before we "commit" them to Git. 

Commit A "commit" is a snapshot of our repository. This way if we ever need to look back at the changes we've made (or if someone else does), we will see a nice timeline of all changes. 

    git commit -m "Add cute octocat story" -  

    git add '*.txt' - adder alle filene som har .txt 

Wildcards: We need quotes so that Git will receive the wildcard before our shell can interfere with it. Without quotes our shell will only execute the wildcard search within the current directory. Git will receive the list of files the shell found instead of the wildcard and it will not be able to add the files inside of the octofamily directory. 

    git log - viser en logg over de forskjellige tingene som en har foretatt seg 

    git branch - lage en ny branch - en ny versjon av objektet 

    git checkout "branchname" - skifte til et annet branch 

    git merge "branchname" - utføre det som har blitt utført i den branchen 

    git branch -d "branchname" - for å slette branches 

 

 
