import matplotlib.pyplot as plt 

def graphSnowFall(t): 
    try: 
        with open(t, 'r') as file:
            snowfall_cm = file.readlines()

            for i in snowfall_cm:
                if (i == '\n'):
                    snowfall_cm.remove(i)

            between_0_and_10 = 0
            between_11_and_20 = 0
            between_21_and_30 = 0
            between_31_and_40 = 0
            between_41_and_50 = 0

            for i in range(0, len(snowfall_cm)):
                snowfall_cm[i].strip()
                snowfall_cm[i] = int(snowfall_cm[i])
                if snowfall_cm[i] <= 10: 
                    between_0_and_10 += 1
                elif snowfall_cm[i] >= 11 and snowfall_cm[i] <= 20: 
                    between_11_and_20 += 1
                elif snowfall_cm[i] >=21 and snowfall_cm[i] <= 30: 
                    between_21_and_30 += 1
                elif snowfall_cm[i] >= 31 and snowfall_cm[i] <= 40: 
                    between_41_and_50+= 1
                else:
                    between_41_and_50 += 1

            x = ['0 - 10', '11 - 20', '21 - 30', '31 - 40', '41 - 50']
            y = [
                between_0_and_10, 
                between_11_and_20, 
                between_21_and_30, 
                between_31_and_40, 
                between_41_and_50
            ]; 
            plt.bar(x, y)
            plt.title('Snowfall')
            plt.xlabel('Range (cm)')
            plt.ylabel('Occurrences')
            plt.yticks([0, 1, 2, 3])
            plt.show() 
            print(snowfall_cm)
            
    except FileNotFoundError: 
        print("File was not found!")

graphSnowFall('data.txt')

