from basic_exercises import *

def Fran(weight):    
    print(" ________ For Time ________ \n")
    
    for i in range(21, 8, -6):
        Thruster(i, weight)
        PullUp(i)
    print(" __________________________ ")
    print(f"\n ==>> Score is time to complete...")
    
def Wod_2024_08_19():
    exercices = [
        {
            'name': DoubleDB_HangCleanAndJerk, 
            'val1': 10, 
            'val2': 22.5
        }, 
        {
            'name': DoubleDB_FrontSquat,
            'val1': 15, 
            'val2': 22.5
        }, 
        {  
            'name': DoubleUnders, 
            'val1': 50
        }
    ]
    print(" ________ AMRAP 6' ________ \n")
    for exo in exercices:
        if 'val2' in exo:
            exo['name'](exo.get('val1'), exo.get('val2'))
        else:
            exo['name'](exo.get('val1')) 
    print(" __________________________ ")   
    print(f"   ==>> Score1 is number of rounds/repetitions...\n")
    
    print("   --  Rest 3'  --\n")
    print(" ________ AMRAP 6' ________ \n")
    for exo in reversed(exercices):
        if 'val2' in exo:
            exo['name'](exo.get('val1'), exo.get('val2'))
        else:
            exo['name'](exo.get('val1'))    
    print(" __________________________ ")
    print(f"   ==>> Score2 is number of rounds/repetitions...")
    
    
    print(f"\n ==>> Score is Score1 | Score2")

if __name__ == '__main__':    
    # Fran("43/30 kgs")
    Wod_2024_08_19()
    