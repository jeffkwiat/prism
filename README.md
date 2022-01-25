# KSums and Salesman Problems

[![Git](https://app.soluble.cloud/api/v1/public/badges/055c5060-4500-4f69-804c-8a443dd10146.svg?orgId=498499820349)](https://app.soluble.cloud/repos/details/github.com/jeffkwiat/prism?orgId=498499820349)  

## How to Install
    git clone https://github.com/jeffkwiat/prism.git
    cd prism
    
## How to Run
    python ksums.py
    python vacationing-salesman.py
    
## Outstanding Issues

- I did not have a chance to implement the more efficient version of KSums
- I would like to add test cases across the board, and given more time, I would have done more TDD.
- I would refactor the vacationing salesman to split out some of the functions from run()
- I would likely create a Leg class that would contain the information for each particular leg, 
including distance, names, etc.
- I would add try/except clauses to catch geopy timeouts, etc.
- I'd probably restructure my app a bit to move the test files into a subdirectory, etc.
- Improve the .gitignore
- More doucmentation is always nice
