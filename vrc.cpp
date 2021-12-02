#include<bits/stdc++.h>

int arr[9],arr1[9];

using namespace std;

void settingParity(int a[])
{
	int count = 0;
    // counting the number of ones
	for(int i = 0; i < 8; i++)
		if(a[i]) count++;
    
    // checking the parity
	if(count%2==0) a[8]=0;
	else a[8]=1;
    
    count = 0;
    // printing the byte
	cout << endl << "VRC: " << endl; 
	for(int i = 0; i < 9; i++)
	{
		if(i==8) cout << " | ";
		cout << a[i] << " ";
	}
}

void toBinary(char letter)
{
	int j = 0;
	int bin = stoi(bitset<8>(letter).to_string());
    
    // insert letter in binary form in arr 
	for(int i = 7; i >= 0; --i)
	{
		arr[i] = bin % 10;
		bin /= 10;
		if(arr[i] == 1) j++;  
	}

    if(j%2 == 0)
        arr[8] = 0;
    else 
        arr[8] = 1;
}


int main()
{       
	char chr1, chr;
	cout << "Data to send: ";
	cin >> chr;
    
    // Converting data to send in binary
	toBinary(chr);
	cout << endl << "Binary of the data sent: ";
	for(int i=0 ; i<8 ; i++)
	{
		arr1[i]=arr[i];
		cout << arr[i] << " ";
	}
    
    // Checking de parity of the data sent
	settingParity(arr);

	cout << "\nData received: ";
    cin >> chr1;
    
    // Converting the received data to binary
    toBinary(chr1);
	cout << endl << endl << "Binary of received data: ";
	for(int i = 0 ; i < 8 ; i++)
		cout << arr[i] << " ";

    // Checking the parity of the received data
	settingParity(arr);
    
}




