from ListNode import *
from LinkedQueue import *

def main():

    #Create the queue
    printer_queue = LinkedQueue()
    printer_queue2 = LinkedQueue()
    
    #Assume that all jobs are submitted almost at the same time in the order
    #found in the file
    my_file = open("printerJobs.txt")

    #Put everything except the heading in the queue
    for each_job in my_file:
        job = each_job.strip()
        #Skip the heading
        if job[0] == 'r':
            continue
     #if room number starts with 3 go to different que   
        if job[0] == '3':
            printer_queue2.enqueue(each_job.strip())
        else:
            printer_queue.enqueue(each_job.strip())
        


        
       

    #This statement is mostly for debugging purposes
    #print(printer_queue)

    #Initialize variables
    #Each time through the printing loop the wait_time increments by 1
    #The wait_time for a particular job is the value stored when the job
    #starts printing.  The wait_time for the first job is 0
    wait_time = 0
    wait_time2 = 0

    #Counter to keep track of total number of jobs (should end up
    #being the length of the queue)
    total_jobs = 0
    total_jobs2 = 0

    #Accumulates the wait times for all of the jobs.  In order to find
    #the average wait time, this number will be divided by the previous
    #number (total_jobs)
    total_wait_time = 0
    total_wait_time2 = 0
       
    #Keep going until all jobs have printed
    while printer_queue.is_empty() == False:
        #Get the printer job from the queue
        job = printer_queue.dequeue()

        #The job that was in the queue is a line of text
        #Split it and cast the second value (index of 1) as an integer
        #to get the number of pages to be printed
        job_details = job.split()
        pages = int(job_details[1])
        rooms = int(job_details[0])

    
        total_jobs += 1
        total_wait_time = wait_time
    

    #Print information about the print job (mostly for debugging purposes)
    #print("total_jobs =", total_jobs)
    #print("pages =", pages)
    #print("total_wait_time =", total_wait_time)

        #Print each page
        for each_page in range(pages):
            #print("printing", each_page + 1, "of", pages, "pages", "in job", total_jobs)
            #Update the wait_time for the next print job
            wait_time += 1
        print("printing", pages, "pages in job", total_jobs)

        #Adds a line of space between jobs
        print()

    #Calculates average wait time for all jobs and prints the total
    avg_wait_time = total_wait_time / total_jobs
    print("The average wait time: ", avg_wait_time)
    print()

#prints the second que till empty

    while printer_queue2.is_empty() == False:
        #Get the printer job from the queue
        job = printer_queue2.dequeue()

        #The job that was in the queue is a line of text
        #Split it and cast the second value (index of 1) as an integer
        #to get the number of pages to be printed
        job_details = job.split()
        pages = int(job_details[1])
        rooms = int(job_details[0])

    
        total_jobs2 += 1
        total_wait_time2 = wait_time2
    

    #Print information about the print job (mostly for debugging purposes)
    #print("total_jobs =", total_jobs)
    #print("pages =", pages)
    #print("total_wait_time =", total_wait_time)

        #Print each page
        for each_page in range(pages):
            #print("printing", each_page + 1, "of", pages, "pages", "in job", total_jobs)
            #Update the wait_time for the next print job
            wait_time2 += 1
        print("printing", pages, "pages in job", total_jobs2)

        #Adds a line of space between jobs
        print()

    #Calculates average wait time for all jobs and prints the total
    avg_wait_time = total_wait_time2 / total_jobs2
    print("The average wait time: ", avg_wait_time)
    print()

    return

main()
