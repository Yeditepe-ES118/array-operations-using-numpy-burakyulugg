import numpy as np

def stat():
    # 1. loads the populations.txt into data variable
    data = np.loadtxt('populations.txt', skiprows=1)
    
    # 2. extracts the Hare column and puts it into hare
    hare = data[:, 1]
    
    # 3. finds the year when the hare population is the lowest
    min_hare_index = np.argmin(hare)
    min_year_hare = data[min_hare_index, 0]
    
    # 4. finds the average of the Lynx population over years
    lynx_avg = np.mean(data[:, 2])
    
    # 5. creates new_data with sum of all species as last column
    species_sum = np.sum(data[:, 1:], axis=1, keepdims=True)
    new_data = np.hstack((data, species_sum))
    
    # 6. makes the Carrot population below 40000 to 0 in new_data
    carrot_col = 3
    carrot_mask = new_data[:, carrot_col] < 40000
    new_data[carrot_mask, carrot_col] = 0
    
    # 7. returns all required variables
    return data, hare, min_year_hare, lynx_avg, new_data