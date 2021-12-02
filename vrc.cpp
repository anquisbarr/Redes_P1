#include<stdio.h>
#include<bits/stdc++.h>
int binary(char);
void parity(int[]);


int arr[9],arr1[9];

using namespace std;

int main()
{       
	char chr1, chr;
	cout << "Ingresar datos: ";
	cin >> chr >> chr1;

	binary(chr);
	cout << endl << "Binary: ";

	for(int i=0 ; i<8 ; i++)
	{
		arr1[i]=arr[i];
		cout << arr[i] << " ";
	}

	parity(arr);
	binary(chr1);
	cout << endl << endl << "Binary : ";
	for(int i = 0 ; i < 8 ; i++)
	{
		cout << arr[i] << " ";
	}
	parity(arr);
}



void parity(int a[])
{
	int count = 0;
	for(int i = 0; i < 8; i++)
		if(a[i]) count++;

	if(count%2==0) a[8]=0;
	else a[8]=1;
	
	count=0;
	cout << endl << "VRC: " << endl; 
	for(int i = 0; i < 9; i++)
	{
		if(i==8) cout << " | ";
		cout << a[i] << " ";
	}
}

int binary(char letter)
{
	int rem;
	int j = 0;

	int bin = stoi(bitset<8>(letter).to_string());

	for(int i = 7; i >= 0; --i)
	{
		arr[i] = bin % 10;
		bin /= 10;
		if(arr[i] == 1) j++;  
	}


	if(j%2==0)
		arr[8] = 0;
	else
		arr[8] = 1;

	return(0);
}