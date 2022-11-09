from preprocessing import strip_emoji
import re

def postprocess(dict):
    final_keys_1 = [ 'Current Job', 'Total Experience(years)', 'Awards'] #str
    final_keys_2 =['Personal Details','Experience','Education'] #dict
    final_keys_0 = ["Skills",'Reference','university','degree','Companies worked at', 'degree'] #list

    personal_keys = ['Name', 'Phone Number', 'Email Id', 'Gender', 'Date of birth', 'Location', 'Pincode']
    exp_keys = ['Designation', 'Company', 'Experience Year', 'Projects']
    edu_keys = ['Degree', 'College', 'Graduation Year', 'Trainings/Courses', 'Publications']
    
    #clean function 
    for i in final_keys_1: #str
        k = dict[i]
        k = strip_emoji(k)
        k = re.sub("\n"," ",k)
        k = re.sub("/n"," ",k)
        k = k.replace("Address:-Email:Address:-","")
        dict[i] = k
        
        
    for i in final_keys_0: #list
        k = dict[i]
        t = 0
        for m in k:
          try:
            m = strip_emoji(m)
            m = re.sub("\n"," ",m)
            m = re.sub("/n"," ",m)
            dict[i][t] = m
            t = t+1
          except:
            pass

    for i in final_keys_2: #dict
        k = dict[i]
        if i == 'Personal Details':
            for m in personal_keys:
                temp = k[m]
                try:
                    temp = strip_emoji(temp)
                    temp = re.sub("\n"," ",temp)
                    temp = re.sub("/n"," ",temp)
                except:
                    pass
                dict['Personal Details'][m] = temp
                
        if i == 'Experience':
            for m in exp_keys:
                temp = k[m]
                try:
                    temp = strip_emoji(temp)
                    temp = re.sub("\n"," ",temp)
                    temp = re.sub("/n"," ",temp)
                except:
                    pass
                dict['Experience'][m] = temp
                
        if i == 'Education':
            for m in edu_keys:
                temp = k[m]
                try:
                    temp = strip_emoji(temp)
                    temp = re.sub("\n"," ",temp)
                    temp = re.sub("/n"," ",temp)
                except:
                    pass
                dict['Education'][m] = temp
    return dict