"""
For robotic palletising, four layers of five objects each.
"""

def Palletzerv1(len, weight, hight, heng_nums, shu_nums, 
            heng_weight, shu_weight, ceng_nums=1, rotate=False):
    
    duo_len = (len*heng_nums)+(heng_weight*(heng_nums-1))#30*2 
    duo_len_= (weight*shu_nums)+(shu_weight*(shu_nums-1))

    # print(Coordinate)
    if duo_len == duo_len_:
        # x= weight//2 ,y=len//2, z = hight  # center point
        if rotate:
            x=len//2
            y=weight//2+(len+shu_weight)
            z=hight*ceng_nums                
            Coordinate = [x,y,z]
            print(Coordinate)
            for _ in range(1, heng_nums):
                Coordinate[0] += (heng_weight + len)
                print(Coordinate)
            print("--------------")
        else:
            x=weight//2
            y=len//2
            z=hight*ceng_nums
            Coordinate_ = [x,y,z]
            print(Coordinate_)
            for _ in range(1, shu_nums):
                Coordinate_[0] += (shu_weight + weight)
                print(Coordinate_)
            print("==============")
            
    else:
        print("Warning!")

    return 
    
def Palletzerv2(len, weight, hight, heng_nums, shu_nums,
            heng_weight, shu_weight, ceng_nums=1, rotate=False):
    
    # out = Maduov2(30,20,8,3,2,10,5,rotate=True)
    duo_len = (len*heng_nums)+(heng_weight*(heng_nums-1))#30*2 
    duo_len_= (weight*shu_nums)+(shu_weight*(shu_nums-1))

    # print(Coordinate)
    if duo_len == duo_len_:
        # x= weight//2 ,y=len//2, z = hight
        if rotate:
            x=weight//2
            y=len//2+(weight+shu_weight)
            z=hight*ceng_nums               
            Coordinate = [x,y,z]
            print(Coordinate)
            for _ in range(1, shu_nums):
                Coordinate[0] += (shu_weight + weight)
                print(Coordinate)
            print("--------------")  
        else:
            y=weight//2
            x=len//2
            z=hight*ceng_nums
            Coordinate_ = [x,y,z]
            print(Coordinate_)
            for _ in range(1, heng_nums):
                Coordinate_[0] += (heng_weight + len)
                print(Coordinate_)
            print("==============")       
    else:
        print("Warning!")
    return

if __name__ == "__main__":
    print("Layer1 coordinates")
    out = Palletzerv1(30,20,4,2,3,10,5)
    out = Palletzerv1(30,20,4,2,3,10,5,rotate=True)
    print("Layer2 coordinates")
    out = Palletzerv2(30,20,4,2,3,10,5,ceng_nums=2,rotate=True)
    out = Palletzerv2(30,20,4,2,3,10,5,ceng_nums=2)
    print("Layer3 coordinates")
    out = Palletzerv1(30,20,4,2,3,10,5,ceng_nums=3,rotate=True)
    out = Palletzerv1(30,20,4,2,3,10,5,ceng_nums=3)
    print("Layer4 coordinates")
    out = Palletzerv2(30,20,4,2,3,10,5,ceng_nums=4,rotate=True)
    out = Palletzerv2(30,20,4,2,3,10,5,ceng_nums=4)
