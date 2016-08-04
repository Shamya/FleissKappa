from fleiss import fleissKappa


if __name__ == "__main__":
    
    print("Example run to calculate Fleiss' Kappa")
    
    print("\nTest case 1 - Fleiss 1971")
    #Fleiss, 1971 example
    rate = \
    [
        [0,0,0,6,0],
        [0,3,0,0,3],
        [0,1,4,0,1],
        [0,0,0,0,6],
        [0,3,0,3,0],
        [2,0,4,0,0],
        [0,0,4,0,2],
        [2,0,3,1,0],
        [2,0,0,4,0],
        [0,0,0,0,6],
        [1,0,0,5,0],
        [1,1,0,4,0],
        [0,3,3,0,0],
        [1,0,0,5,0],
        [0,2,0,3,1],
        [0,0,5,0,1],
        [3,0,0,1,2],
        [5,1,0,0,0],
        [0,2,0,4,0],
        [1,0,2,0,3],
        [0,0,0,0,6],
        [0,1,0,5,0],
        [0,2,0,1,3],
        [2,0,0,4,0],
        [1,0,0,4,1],
        [0,5,0,1,0],
        [4,0,0,0,2],
        [0,2,0,4,0],
        [1,0,5,0,0],
        [0,0,0,0,6]
    ]
    kappa = fleissKappa(rate,6)
    assert(kappa==0.43)
    
    print("\nTest case 2 - Wikipedia example")
    #wikipedia example
    rate = \
    [
        [0,0,0,0,14],
        [0,2,6,4,2],
        [0,0,3,5,6],
        [0,3,9,2,0],
        [2,2,8,1,1],
        [7,7,0,0,0],
        [3,2,6,3,0],
        [2,5,3,2,2],
        [6,5,2,1,0],
        [0,2,2,3,7]
    ]
    kappa = fleissKappa(rate,14)
    assert(kappa==0.21)
    
    print("\nTest case 3 - perfect agreement")
    #kappa = 1
    rate = \
    [
        [2,0,0,0],
        [0,2,0,0],
        [0,0,2,0],
        [0,0,0,2]
    ]
    kappa = fleissKappa(rate,2)
    assert(kappa==1)
    
    print("\nTest case 4 - perfect expected agreement")
    #kappa = -inf (not defined as divide by 0)
    rate = \
    [
        [2,0,0,0],
        [2,0,0,0],
        [2,0,0,0],
        [2,0,0,0]
    ]
    kappa = fleissKappa(rate,2)
    assert(kappa==-float("inf"))