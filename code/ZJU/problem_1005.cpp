#include <iostream>
#include <algorithm>

using namespace std;
/*定义学生类，class和struct其实一个样，可以直接变为结构体*/
class Student
{
public:
        int id;
        int ge;
        int gi;
        int choice[5];
};
/*定义学校类*/
class School
{
public:
        int quota;
        Student std[100];
        int front,rear;
};
/*学生成绩排序函数*/
bool cmp(Student a,Student b)
{
        if(a.ge+a.gi!=b.ge+b.gi )
                return a.ge+a.gi>b.ge+b.gi;
        else
                return a.ge>b.ge;
}
/*学生id排序函数*/
bool cmpa(Student a,Student b)
{
        return a.id<b.id;
}

int main()
{
        int n,m,k;
        int i,j;
        while(cin>>n>>m>>k)
        {
                Student std[100];
                School sch[100];
                /*学校信息录入*/
                for(i=0;i!=m;i++)
                {
                        cin>>sch[i].quota;
                        sch[i].front=0;
                        sch[i].rear=0;
                }
                /*学生信息录入*/
                for(i=0;i!=n;i++)
                {
                        cin>>std[i].ge>>std[i].gi;
                        for(j=0;j!=k;j++)
                                cin>>std[i].choice[j];
                        std[i].id=i;
                }
                /*学生成绩排序*/
                sort(std,std+n,cmp);
                /*按学生成绩从高到低分配学校*/
                for(i=0;i!=n;i++)
                {
                        /*按志愿先后选择学校*/
                        for(j=0;j!=k;j++)
                        {
                                /*学校还有名额时，直接入该学校的队列*/
                                if(sch[std[i].choice[j]].quota>0)
                                {
                                        sch[std[i].choice[j]].std[sch[std[i].choice[j]].rear++]=std[i];        
                                        sch[std[i].choice[j]].quota--;
                                        break;
                                }
                                /*学校没有名额时，成绩是否与最后一名录取的学生相同，同则进*/
                                else if(std[i].ge==sch[std[i].choice[j]].std[sch[std[i].choice[j]].rear-1].ge
                                        &&std[i].gi==sch[std[i].choice[j]].std[sch[std[i].choice[j]].rear-1].gi)
                                {
                                        sch[std[i].choice[j]].std[sch[std[i].choice[j]].rear++]=std[i];        
                                        sch[std[i].choice[j]].quota--;
                                        break;
                                }
                        }
                }
                /*输出每个学校录取者的id*/
                for(i=0;i!=m;i++)
                {
                        if(sch[i].front==sch[i].rear)
                                cout<<endl;
                        else
                        {
                                /*学生id排序*/
                                sort(sch[i].std,sch[i].std+sch[i].rear,cmpa);
                                cout<<sch[i].std[sch[i].front++].id;
                                while(sch[i].front!=sch[i].rear)
                                        cout<<' '<<sch[i].std[sch[i].front++].id;
                                cout<<endl;
                        }        
                }

        }
        return 0;
}