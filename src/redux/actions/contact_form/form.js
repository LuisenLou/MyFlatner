import {
    FORM_SUBMIT_REQUEST,
    FORM_SUBMIT_SUCCESS,
    FORM_SUBMIT_FAILURE,
    FORM_SUBMIT_COMPLETE,
  } from './types';

import axios from 'axios'


export const submitForm = (formData) => async dispatch => {


    dispatch({
        type:FORM_SUBMIT_REQUEST
    });

    try{
        const res = await axios.post('http://localhost:8000/api/contact/', formData,{
            withCredentials: true,
            headers: {
                'Content-Type': 'application/json',
            },
        });
        
        dispatch({
            type: FORM_SUBMIT_SUCCESS,
            payload: res.data
        });
        
    }catch(err){
        dispatch({
            type:FORM_SUBMIT_FAILURE,
            payload: err.response ? err.response.data : 'Hubo un error al enviar el formulario',
        })
    } finally {
        dispatch({
            type: FORM_SUBMIT_COMPLETE,
        });
    }
};