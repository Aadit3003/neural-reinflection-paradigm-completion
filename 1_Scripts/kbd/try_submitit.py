import submitit
from prep import main as m1
from baseline import predict

def add(a, b):
    return a + b

# executor is the submission interface (logs are dumped in the folder)
executor = submitit.AutoExecutor(folder="log_test")
# set timeout in min, and partition for running the job

executor.update_parameters(slurm_partition="debug")
job = executor.submit(add, 5, 7)  # will compute add(5, 7)
print(job.job_id)  # ID of your job
output = job.result()  # waits for completion and returns output
print(output)
print()

job = executor.submit(m1)
print(job.job_id) 
output = job.result() 
print(output)
print()

job = executor.submit(predict, "kbd", "dev", "../../dataset/kbd.train.tsv")
print(job.job_id) 
output = job.result() 
print(output)
print()

job = executor.submit(predict, "kbd", "dev", "../../dataset/kbd.train_2_simple_addition.tsv")
print(job.job_id) 
output = job.result() 
print(output)
print()

job = executor.submit(predict, "kbd", "dev", "../../dataset/kbd.train_3_self_pollinate.tsv")
print(job.job_id) 
output = job.result() 
print(output)
print()

job = executor.submit(predict, "kbd", "dev", "../../dataset/kbd.train_4_cross_pollinate.tsv")
print(job.job_id) 
output = job.result() 
print(output)
print()

job = executor.submit(predict, "kbd", "test", "../../dataset/kbd.train_2_simple_addition.tsv")
print(job.job_id) 
output = job.result() 
print(output)
print()