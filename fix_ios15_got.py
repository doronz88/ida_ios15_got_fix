import idautils
import idc

for seg_start in idautils.Segments():
	seg_name = idc.get_segm_name(seg_start)
	if seg_name != '__got':
		continue

	seg_end = idc.get_segm_end(seg_start)

	for ea in range(seg_start, seg_end, 8):
		symbol_name = idc.get_name(ea)

		if '_ptr' not in symbol_name:
			print('cannot fix: {}'.format(symbol_name))
			continue

		# print('fixing: {}'.format(symbol_name))

		symbol_name = symbol_name.split('_ptr')[0]
		correct_value = idc.get_name_ea_simple('__imp_' + symbol_name)

		if correct_value == idc.BADADDR:
			correct_value = idc.get_name_ea_simple(symbol_name)
			if correct_value == idc.BADADDR:
				continue

		idc.patch_qword(ea, correct_value)
