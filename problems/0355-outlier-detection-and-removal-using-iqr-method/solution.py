import numpy as np

def detect_outliers_iqr(data: list[float], k: float = 1.5) -> dict:
	"""
	Detect and remove outliers using the IQR method.
	
	Args:
		data: List of numerical values
		k: IQR multiplier for determining outlier bounds (default 1.5)
	
	Returns:
		Dictionary with 'cleaned_data', 'outlier_indices', 'lower_bound', 'upper_bound'
	"""
	# Your code here

	q1 = np.percentile(data, 25)
	q3 = np.percentile(data, 75)
	iqr = q3 - q1 
	lower_bound  = q1 - (k * iqr)
	upper_bound = q3 + (k * iqr)

	outlier_indices = [
		i
		for i , x in enumerate(data)
		if x < lower_bound or x > upper_bound
	]

	cleaned_data = [
		round(x, 4)
		for x in data
			if lower_bound <= x <= upper_bound 

	]

	return {"cleaned_data": cleaned_data,
	"outlier_indices": outlier_indices
	, "lower_bound":lower_bound
	, "upper_bound" : upper_bound
	}
	pass