import wiringpi2 as gpio

owpin = 8  # 第8脚为1-wire脚


def getval(owpin):
    tl = []  # 存放每个数据位的时间
    tb = []  # 存放数据位
    gpio.wiringPiSetup()  # 初始化wiringpi库
    gpio.pinMode(owpin, 1)  # 设置针脚为输出状态
    gpio.digitalWrite(owpin, 1)  # 输出高电平
    gpio.delay(1)
    gpio.digitalWrite(owpin, 0)  # 拉低20ms开始指令
    gpio.delay(25)
    gpio.digitalWrite(owpin, 1)  # 抬高20-40us
    gpio.delayMicroseconds(20)
    gpio.pinMode(owpin, 0)  # 设针脚为输入状态
    while (gpio.digitalRead(owpin) == 1): pass  # 等待DHT11拉低管脚

    for i in range(45):  # 测试每个数据周期的时间（包括40bit数据加一个发送开始标志
        tc = gpio.micros()  # 记下当前us数（从初始化开始算起，必要时重新初始化）
        '''
        一个数据周期，包括一个低电平，一个高电平，从DHT11第一次拉低信号线开始
        到DHT11发送最后一个50us的低电平结束（然后被拉高，一直维持高电平，所以
        最后的完成标志是一直为高，超过500ms）
        '''
        while (gpio.digitalRead(owpin) == 0): pass
        while (gpio.digitalRead(owpin) == 1):
            if gpio.micros() - tc > 500:  # 如果超过500ms就结束了
                break
        if gpio.micros() - tc > 500:  # 跳出整个循环
            break
        tl.append(gpio.micros() - tc)  # 记录每个周期时间的us数，存到tl这个列表

    #    print(tl)      #反注释后可打印时间列表
    tl = tl[1:]  # 去掉第一项，剩下40个数据位
    for i in tl:
        if i > 100:  # 若数据位为1，时间为50us低电平+70us高电平=120us
            tb.append(1)
        else:
            tb.append(0)  # 若数据位为0，时间为50us低电平+25us高电平=75us
            # 这里取大于100us就为1
    #    print(tb)      #反注释可查看每一位状态
    return tb


def GetResult(owpin):
    for i in range(10):
        SH = 0;
        SL = 0;
        TH = 0;
        TL = 0;
        C = 0
        result = getval(owpin)
        #        print(len(result))
        if len(result) == 40:
            for i in range(8):
                # 计算每一位的状态，每个字8位，以此为湿度整数，湿度小数，温度整数，温度小数，校验和
                SH *= 2;
                SH += result[i]
                SL *= 2;
                SL += result[i + 8]
                TH *= 2;
                TH += result[i + 16]
                TL *= 2;
                TL += result[i + 24]
                C *= 2;
                C += result[i + 32]
            if ((SH + SL + TH + TL) % 256) == C and C != 0:
                break
            else:
                print("Read Sucess,But checksum error! retrying")
        else:
            print("Read failer! Retrying")
        gpio.delay(200)
    return SH, SL, TH, TL


SH, SL, TH, TL = GetResult(owpin)
print("湿度:", SH, SL, "温度:", TH, TL)