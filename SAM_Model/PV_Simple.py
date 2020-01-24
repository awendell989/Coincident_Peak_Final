from PySSC import PySSC
if __name__ == "__main__":
	ssc = PySSC()
	print ('Current folder = /Users/Avery/Desktop/Energy_Project/SAM_Model')
	print ('SSC Version = ', ssc.version())
	print ('SSC Build Information = ', ssc.build_info().decode("utf - 8"))
	ssc.module_exec_set_print(0)
	data = ssc.data_create()
	ssc.data_set_string( data, b'solar_resource_file', b'/Users/Avery/SAM Downloaded Weather Files/14825_42.046821_-76.618011_psmv3_60_tmy.csv' );
	ssc.data_set_number( data, b'system_capacity', 23000 )
	ssc.data_set_number( data, b'module_type', 0 )
	ssc.data_set_number( data, b'dc_ac_ratio', 1.1499999761581421 )
	ssc.data_set_number( data, b'inv_eff', 96 )
	ssc.data_set_number( data, b'losses', 14.075660705566406 )
	ssc.data_set_number( data, b'array_type', 0 )
	ssc.data_set_number( data, b'tilt', 20 )
	ssc.data_set_number( data, b'azimuth', 180 )
	ssc.data_set_number( data, b'gcr', 0.40000000596046448 )
	ssc.data_set_number( data, b'adjust:constant', 0 )
	module = ssc.module_create(b'pvwattsv5')	
	ssc.module_exec_set_print( 0 );
	if ssc.module_exec(module, data) == 0:
		print ('pvwattsv5 simulation error')
		idx = 1
		msg = ssc.module_log(module, 0)
		while (msg != None):
			print ('	: ' + msg.decode("utf - 8"))
			msg = ssc.module_log(module, idx)
			idx = idx + 1
		SystemExit( "Simulation Error" );
	ssc.module_free(module)
	annual_energy = ssc.data_get_number(data, b'annual_energy');
	print ('Annual energy (year 1) = ', annual_energy)
	capacity_factor = ssc.data_get_number(data, b'capacity_factor');
	print ('Capacity factor (year 1) = ', capacity_factor)
	kwh_per_kw = ssc.data_get_number(data, b'kwh_per_kw');
	print ('Energy yield (year 1) = ', kwh_per_kw)
	ssc.data_free(data);