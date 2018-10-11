for fn in /media/sf_VMs/share/headdata/*.csv 
do 
python3 /media/sf_VMs/share/make_fields.py $fn 
done
