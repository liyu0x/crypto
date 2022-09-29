# have some bugs, fixing


# PRESENT CIPHER DDT

![DDT](https://github.com/liyu0x/crypto/blob/main/Present/ddt.jpg?raw=true)

# RUN CODE RESULT

```
round-0:[input differ: -0x1,output differ(p-boxed): 0x1,w=1, all active boxes:0] round-1:[input differ: 0x1,output differ(p-boxed): 0x10001,w=2,all active boxes:1] round-2:[input differ: 0x10001,output differ(p-boxed): 0x110011,w=6,all active boxes:3] round-3:[input differ: 0x110011,output differ(p-boxed): 0x330033,w=14,all active boxes:7] round-4:[input differ: 0x330033,output differ(p-boxed): 0x3300330000,w=22,all active boxes:11] 

round-0:[input differ: -0x1,output differ(p-boxed): 0x1,w=1, all active boxes:0] round-1:[input differ: 0x1,output differ(p-boxed): 0x10001,w=2,all active boxes:1] round-2:[input differ: 0x10001,output differ(p-boxed): 0x110011,w=6,all active boxes:3] round-3:[input differ: 0x110011,output differ(p-boxed): 0x2000330033,w=22,all active boxes:7] round-4:[input differ: 0x2000330033,output differ(p-boxed): 0x23302320001,w=31,all active boxes:12] 

round-0:[input differ: -0x1,output differ(p-boxed): 0x1,w=1, all active boxes:0] round-1:[input differ: 0x1,output differ(p-boxed): 0x10001,w=2,all active boxes:1] round-2:[input differ: 0x10001,output differ(p-boxed): 0x110011,w=6,all active boxes:3] round-3:[input differ: 0x110011,output differ(p-boxed): 0x3000330033,w=54,all active boxes:7] round-4:[input differ: 0x3000330033,output differ(p-boxed): 0x23302330000,w=64,all active boxes:12] 

round-0:[input differ: -0x1,output differ(p-boxed): 0x1,w=1, all active boxes:0] round-1:[input differ: 0x1,output differ(p-boxed): 0x10001,w=2,all active boxes:1] round-2:[input differ: 0x10001,output differ(p-boxed): 0x110011,w=6,all active boxes:3] round-3:[input differ: 0x110011,output differ(p-boxed): 0x30000000030033,w=94,all active boxes:7] round-4:[input differ: 0x30000000030033,output differ(p-boxed): 0x201320130000,w=102,all active boxes:11] 

```

pattern: ```[input_different, output_different(P boxed), probability, all active boxes]```

probability: ```w/(2^(num of active boxes * 16))```

# run code:

```python3 compute_differential_trail.py```

