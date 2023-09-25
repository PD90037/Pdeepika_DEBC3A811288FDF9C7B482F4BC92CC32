Stringlinner[]={"11","21","31","32",
                            "33","23","13","12"}:
            
45-Degreerotatio
for(int i=0;i<5;i++){
                for(int j=0;j<5;j++){
                    // Transform outer portion
                    for(int k=0; k<outer.length; k++){
                        char indices[]=outer[k].toCharArray();
                        int a = Integer.parseInt(String.valueOf(indices[0]));
                        int b = Integer.parseInt(String.valueOf(indices[1]));
                        if(a==i && b==j){
                            if(k==15){k=1;}
                            else if(k==14){k=0;}
                            else {k+=2;}
                            indices=outer[k].toCharArray();
                            a = Integer.parseInt(String.valueOf(indices[0]));
                            b = Integer.parseInt(String.valueOf(indices[1]));
                            tra[a][b] = arr[i][j];
                            break;
                        }
                    }
                    // Transform inner portion
                    for(int k=0; k<inner.length; k++){
                        char indices[]=inner[k].toCharArray();
                        int a = Integer.parseInt(String.valueOf(indices[0]));
                        int b = Integer.parseInt(String.valueOf(indices[1]));
                        if(a==i && b==j){
                            if(k==7){k=0;}
                            else {k+=1;}
                            indices=inner[k].toCharArray();
                            a = Integer.parseInt(String.valueOf(indices[0]));
                            b = Integer.parseInt(String.valueOf(indices[1]));
                            tra[a][b] = arr[i][j];
                            break;
                        }
                    }
                    // Keeping center same
                    tra[2][2] = arr[2][2];
                }
            }
Print the transformed output 
for(int i=0;i<5;i++){
                for(int j=0;j<5;j++){
                    System.out.print(tra[i][j]);
                }
                System.out.println();
}