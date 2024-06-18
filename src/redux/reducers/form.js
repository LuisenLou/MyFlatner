import {
    FORM_SUBMIT_REQUEST,
    FORM_SUBMIT_SUCCESS,
    FORM_SUBMIT_FAILURE,
    FORM_SUBMIT_COMPLETE,
  } from '../actions/contact_form/types';
  
  const initialState = {
    loading: false,
    successMessage: null,
    errorMessage: null
  };
  
  export default function submitForm (state = initialState, action){
        const {type, payload} = action;

        switch(type){
            
            case FORM_SUBMIT_REQUEST:
                return{
                    ...state,
                    loading:true,
                    successMessage: null,
                    errorMessage: null,
                }
            case FORM_SUBMIT_SUCCESS:
                return{
                    ...state,
                    successMessage: payload.message,
                    errorMessage: null,
                }
            case FORM_SUBMIT_FAILURE:
                return{
                    ...state,
                    loading: false,
                    successMessage:null,
                    errorMessage: payload.message
                }
            case FORM_SUBMIT_COMPLETE:
                return{
                    ...state,
                    loading: false,
                }

            default:   
                return state
        }
  }