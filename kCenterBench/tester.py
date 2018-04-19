import sys
import subprocess

def test(prog_path,input_path,method,timeout):
  with subprocess.Popen([prog_path,"-i",input_path,"-m",method,"-f","pmed"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True) as process:
    try:
      process.wait(timeout=timeout)
      output = process.stdout.read()
      errput = process.stderr.read()
      if process.returncode == 0:
        solution,execution_time = output.strip().split(',')
        return {
            'status': 'OK',
            'solution': solution,
            'execution_time': execution_time}
      else:
        return {
            'status': 'FAIL',
            'returncode': process.returncode,
            'stdout': output,
            'stderr': errput}
    except subprocess.TimeoutExpired:
      process.kill()
      return {'status': 'TIMEOUT'}
      
def main():
  timeout = 5000
	# print("testing once")
	# result = test("/home/miha/kCenterBench/kCenterBench/main","samples/pmed/pmed1.txt","greedy",5000)
	# print(result)
	# if result['status'] == "OK":
	# 	print("OK")
	# 	print(f"Solution: {result['solution']}, Time: {result['execution_time']} ms")
	# else:
	# 	print("neki je slo narobe")
  for i in range(1,41):
    result = test("/home/miha/kCenterBench/kCenterBench/main",f"samples/pmed/pmed{i}.txt","CDS",timeout)
    if result['status'] == "OK":
      print(f"pmed{i:2}: {result['solution']:4} {result['execution_time']:5} ms")
    elif result['status'] == "TIMEOUT":
      print(f"timeout({timeout}s)")
    else:
     print("ERROR")
     print(f"stdout:\n{result['stdout']}\nstderr:\n{result['stderr']}\n")
if __name__ == '__main__':
  main()
