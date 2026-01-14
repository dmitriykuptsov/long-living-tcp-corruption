d1<-scan("seq_progress.dat")
d2<-scan("ack_seq_progress.dat")

pdf("sequence_progress.pdf")

par(mfrow = c(2, 1))

plot(d1, type="l", col="dark red", lwd=4, xlab="Packet", ylab="Sequence", main="Server-Client")
grid(lwd=2)
plot(d2, type="l", col="dark blue", lwd=4, ylab="Sequence", xlab="Packet", main="Client-Server")
grid(lwd=2)
dev.off()

