# Matiss Laksevics, 4.grupa, IT, DITF, 221RDB363
# python3
import heapq

def parallel_processing(n, m, data):
    threads = [(0, i) for i in range(n)]
    jobs = [(t, i) for i, t in enumerate(data)]
    heapq.heapify(jobs)
    output = []
    while jobs:
        t, i = heapq.heappop(jobs)
        start_time, thread_idx = heapq.heappop(threads)
        output.append((thread_idx, start_time))
        heapq.heappush(threads, (start_time + t, thread_idx))
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    output = parallel_processing(n, m, data)
    for thread_idx, start_time in output:
        print(thread_idx, start_time)

if __name__ == "__main__":
    main()
