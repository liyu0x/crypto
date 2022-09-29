# PRESENT CIPHER DDT

![DDT](https://github.com/liyu0x/crypto/blob/main/Present/ddt.jpg?raw=true)

# RUN CODE RESULT

```
round-0:[input differ: -0x1,output differ(p-boxed): 0x1,w=1, all active boxes:0] round-1:[input differ: 0x1,output differ(p-boxed): 0x10001,w=4,all active boxes:1] round-2:[input differ: 0x10001,output differ(p-boxed): 0x110011,w=64,all active boxes:3] round-3:[input differ: 0x110011,output differ(p-boxed): 0x330033,w=16384,all active boxes:7] round-4:[input differ: 0x330033,output differ(p-boxed): 0x3300330000,w=4194304,all active boxes:11] 

round-0:[input differ: -0x1,output differ(p-boxed): 0x1,w=1, all active boxes:0] round-1:[input differ: 0x1,output differ(p-boxed): 0x10001,w=4,all active boxes:1] round-2:[input differ: 0x10001,output differ(p-boxed): 0x110011,w=64,all active boxes:3] round-3:[input differ: 0x110011,output differ(p-boxed): 0x2000330033,w=4194304,all active boxes:7] round-4:[input differ: 0x2000330033,output differ(p-boxed): 0x23302320001,w=2147483648,all active boxes:12] 

round-0:[input differ: -0x1,output differ(p-boxed): 0x1,w=1, all active boxes:0] round-1:[input differ: 0x1,output differ(p-boxed): 0x10001,w=4,all active boxes:1] round-2:[input differ: 0x10001,output differ(p-boxed): 0x110011,w=64,all active boxes:3] round-3:[input differ: 0x110011,output differ(p-boxed): 0x3000330033,w=18014398509481984,all active boxes:7] round-4:[input differ: 0x3000330033,output differ(p-boxed): 0x23302330000,w=18446744073709551616,all active boxes:12] 

round-0:[input differ: -0x1,output differ(p-boxed): 0x1,w=1, all active boxes:0] round-1:[input differ: 0x1,output differ(p-boxed): 0x10001,w=4,all active boxes:1] round-2:[input differ: 0x10001,output differ(p-boxed): 0x110011,w=64,all active boxes:3] round-3:[input differ: 0x110011,output differ(p-boxed): 0x30000000030033,w=19807040628566084398385987584,all active boxes:7] round-4:[input differ: 0x30000000030033,output differ(p-boxed): 0x201320130000,w=5070602400912917605986812821504,all active boxes:11] 

round-0:[input differ: -0x1,output differ(p-boxed): 0x1,w=1, all active boxes:0] round-1:[input differ: 0x1,output differ(p-boxed): 0x10001,w=4,all active boxes:1] round-2:[input differ: 0x10001,output differ(p-boxed): 0x110011,w=64,all active boxes:3] round-3:[input differ: 0x110011,output differ(p-boxed): 0x30002000030033,w=5070602400912917605986812821504,all active boxes:7] round-4:[input differ: 0x30002000030033,output differ(p-boxed): 0x221322110002,w=2596148429267413814265248164610048,all active boxes:12] 


```

pattern: ```[input_different, output_different(P boxed), probability, all active boxes]```

probability: ```w/(2^(num of active boxes * 16))```

# run code:

```python3 compute_differential_trail.py```

