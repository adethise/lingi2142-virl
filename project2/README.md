# Reflections about projet 2

1. If we have to implement separately the 2 paths, we know that we could do it with tuning the IGP costs and the local prefs. 
2. BUT, we realize that this technique **does not allow us to implement the two 2 paths concurrently**. For instance, the Green path implies that shortest path from C2 to C3 is via E3, while the Blue path implies that shortest path from C2 to C3 is directly via C3, this is incompatible.
3. SO, **we need traffic engineering capabilities**. We thus have 2 options: RSVP-TE or SegmentRouting.

### RSVP-TE
- Can we implement the blue path with RSVP-TE?
- How to make it load balance on two paths between C1 and C3?
- We are not sure if we can do that. We believe we can't but we should investigate more.

### SegmentRouting
- **With segment routing, we are sure that we can implement the blue path**. Using "global segments", the packet will follow the shortest path to the node, and will use ECMP if present. So, we simply have to make sure that C1-C2-C3 and C1-C3 have the same total cost and activate ECMP.
- BUT, we believe segment routing is not implemented on Cisco routers.
- However, we can distribute the labels by “hand” on the routers to **simulate segment routing**. Only 2 paths to setup on a small number of routers, this should not take too long.
- How to configure the ingress router to stack the proper set of labels on incoming packets? Also, how to specify on which packets it should be stacked? based on the IP-Address/Interface? And how to tell it to use basic IP fowarding for the rest of the packets.